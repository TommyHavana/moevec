defmodule MeeWeb.Plugs.VerifyWebhook do
  @moduledoc """
  Verifica webhooks firmados de moevec.org.

  Cabeceras esperadas:
    * `x-mee-timestamp`: segundos Unix del envío
    * `x-mee-signature`: `sha256=` + HMAC-SHA256 en hex de `"<timestamp>.<cuerpo crudo>"`

  Rechaza firmas inválidas y envíos con más de 5 minutos de diferencia (anti-replay).
  El secreto se lee de `config :mee, :moevec_webhook_secret`.
  """
  import Plug.Conn

  @tolerance_seconds 300

  def init(opts), do: opts

  def call(conn, _opts) do
    secret = Application.get_env(:mee, :moevec_webhook_secret)

    with true <- is_binary(secret) and byte_size(secret) >= 32,
         [ts] <- get_req_header(conn, "x-mee-timestamp"),
         [sig] <- get_req_header(conn, "x-mee-signature"),
         {ts_int, ""} <- Integer.parse(ts),
         true <- abs(System.system_time(:second) - ts_int) <= @tolerance_seconds,
         "sha256=" <> given <- sig,
         expected <- sign(secret, ts, MeeWeb.CacheBodyReader.raw_body(conn)),
         true <- Plug.Crypto.secure_compare(expected, String.downcase(given)) do
      conn
    else
      _ ->
        conn
        |> put_resp_content_type("application/json")
        |> send_resp(401, ~s({"error":"firma no válida"}))
        |> halt()
    end
  end

  def sign(secret, timestamp, body) do
    :crypto.mac(:hmac, :sha256, secret, [timestamp, ".", body])
    |> Base.encode16(case: :lower)
  end
end
