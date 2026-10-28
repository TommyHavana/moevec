defmodule Mee.Integrations.ExternalArticle do
  @moduledoc "Artículo publicado fuera de la red (blog de moevec.org) y sincronizado por webhook."
  use Ecto.Schema
  import Ecto.Changeset

  schema "external_articles" do
    field :source, :string
    field :external_id, :string
    field :url, :string
    field :title, :string
    field :excerpt, :string
    field :status, Ecto.Enum, values: [:published, :withdrawn], default: :published
    field :published_at, :utc_datetime

    belongs_to :area, Mee.Atlas.Area

    timestamps(type: :utc_datetime)
  end

  def changeset(article, attrs) do
    article
    |> cast(attrs, [:source, :external_id, :url, :title, :excerpt, :status, :area_id, :published_at])
    |> validate_required([:source, :external_id, :url, :title, :published_at])
    |> validate_length(:title, max: 500)
    |> validate_length(:excerpt, max: 2_000)
    |> validate_change(:url, fn :url, url ->
      case URI.parse(url) do
        %URI{scheme: "https", host: host} when is_binary(host) -> []
        _ -> [url: "debe ser una URL https"]
      end
    end)
    |> unique_constraint([:source, :external_id])
  end
end
