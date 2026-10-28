defmodule Mee.Integrations do
  @moduledoc """
  Integración con moevec.org (WordPress).

  * Entrada: el blog avisa por webhook firmado cuando publica, actualiza o retira
    un artículo (`upsert_article/1`, `withdraw_article/2`).
  * Salida: la API JSON pública (`MeeWeb.Api.*`) expone el mapa y la actividad
    reciente para que WordPress la muestre.
  """
  import Ecto.Query
  alias Mee.Repo
  alias Mee.Atlas.Area
  alias Mee.Integrations.ExternalArticle

  @source "moevec"

  @doc """
  Crea o actualiza un artículo a partir del payload del webhook.
  `area_slug` se resuelve contra el mapa; si no existe, el artículo queda sin área.
  """
  def upsert_article(%{"id" => id} = payload) do
    attrs = %{
      source: @source,
      external_id: to_string(id),
      url: payload["url"],
      title: payload["title"],
      excerpt: payload["excerpt"],
      status: :published,
      area_id: area_id(payload["area_slug"]),
      published_at: parse_datetime(payload["published_at"])
    }

    (Repo.get_by(ExternalArticle, source: @source, external_id: attrs.external_id) ||
       %ExternalArticle{})
    |> ExternalArticle.changeset(attrs)
    |> Repo.insert_or_update()
  end

  def upsert_article(_), do: {:error, :missing_id}

  def withdraw_article(external_id) do
    from(a in ExternalArticle,
      where: a.source == @source and a.external_id == ^to_string(external_id)
    )
    |> Repo.update_all(set: [status: :withdrawn, updated_at: DateTime.utc_now(:second)])

    :ok
  end

  def list_articles(area_id, limit \\ 5) do
    ExternalArticle
    |> where([a], a.status == :published)
    |> then(fn q -> if area_id, do: where(q, [a], a.area_id == ^area_id), else: q end)
    |> order_by([a], desc: a.published_at)
    |> limit(^limit)
    |> Repo.all()
  end

  defp area_id(nil), do: nil
  defp area_id(slug), do: Repo.one(from a in Area, where: a.slug == ^slug, select: a.id)

  defp parse_datetime(value) when is_binary(value) do
    case DateTime.from_iso8601(value) do
      {:ok, dt, _offset} -> DateTime.truncate(dt, :second)
      _ -> nil
    end
  end

  defp parse_datetime(_), do: nil
end
