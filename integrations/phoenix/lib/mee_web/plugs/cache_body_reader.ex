defmodule MeeWeb.CacheBodyReader do
  @moduledoc """
  Guarda el cuerpo crudo de las peticiones a /api/webhooks para poder
  verificar la firma HMAC después de que Plug.Parsers decodifique el JSON.
  Se configura en el endpoint: `body_reader: {MeeWeb.CacheBodyReader, :read_body, []}`.
  """

  def read_body(%Plug.Conn{request_path: "/api/webhooks/" <> _} = conn, opts) do
    case Plug.Conn.read_body(conn, opts) do
      {:ok, body, conn} ->
        {:ok, body, update_in(conn.assigns[:raw_body], &[body | &1 || []])}

      {:more, body, conn} ->
        {:more, body, update_in(conn.assigns[:raw_body], &[body | &1 || []])}

      other ->
        other
    end
  end

  def read_body(conn, opts), do: Plug.Conn.read_body(conn, opts)

  def raw_body(conn) do
    conn.assigns |> Map.get(:raw_body, []) |> Enum.reverse() |> IO.iodata_to_binary()
  end
end
