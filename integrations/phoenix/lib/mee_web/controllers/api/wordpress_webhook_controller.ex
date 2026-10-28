defmodule MeeWeb.Api.WordpressWebhookController do
  @moduledoc """
  POST /api/webhooks/moevec — recibe eventos del blog de moevec.org.

  Cuerpo JSON:
      {"event": "post.published" | "post.updated" | "post.withdrawn",
       "post": {"id": 123, "url": "https://moevec.org/...", "title": "...",
                "excerpt": "...", "area_slug": "trabajo",
                "published_at": "2026-10-28T10:00:00+00:00"}}

  La firma la valida `MeeWeb.Plugs.VerifyWebhook` antes de llegar aquí.
  Es idempotente: repetir el mismo evento no duplica nada.
  """
  use MeeWeb, :controller

  alias Mee.Integrations

  def create(conn, %{"event" => event, "post" => post}) when event in ~w(post.published post.updated) do
    case Integrations.upsert_article(post) do
      {:ok, article} ->
        json(conn, %{ok: true, id: article.id})

      {:error, %Ecto.Changeset{} = cs} ->
        conn |> put_status(422) |> json(%{ok: false, errors: errors(cs)})

      {:error, reason} ->
        conn |> put_status(422) |> json(%{ok: false, error: to_string(reason)})
    end
  end

  def create(conn, %{"event" => "post.withdrawn", "post" => %{"id" => id}}) do
    :ok = Integrations.withdraw_article(id)
    json(conn, %{ok: true})
  end

  def create(conn, _params) do
    conn |> put_status(400) |> json(%{ok: false, error: "evento no soportado"})
  end

  defp errors(changeset) do
    Ecto.Changeset.traverse_errors(changeset, &MeeWeb.CoreComponents.translate_error/1)
  end
end
