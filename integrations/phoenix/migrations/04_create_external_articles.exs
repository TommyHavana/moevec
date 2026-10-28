defmodule Mee.Repo.Migrations.CreateExternalArticles do
  use Ecto.Migration

  def change do
    create table(:external_articles) do
      # "moevec" para el WordPress de moevec.org
      add :source, :string, null: false
      add :external_id, :string, null: false
      add :url, :string, null: false, size: 2048
      add :title, :string, null: false, size: 500
      add :excerpt, :text
      add :status, :string, null: false, default: "published"
      add :area_id, references(:areas, on_delete: :nilify_all)
      add :published_at, :utc_datetime, null: false
      timestamps(type: :utc_datetime)
    end

    create unique_index(:external_articles, [:source, :external_id])
    create index(:external_articles, [:area_id, :status, "published_at DESC"])
  end
end
