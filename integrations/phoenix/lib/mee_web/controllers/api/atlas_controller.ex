defmodule MeeWeb.Api.AtlasController do
  @moduledoc """
  GET /api/v1/areas — el mapa completo con las URL equivalentes en ambos sitios.
  Es la fuente única de la taxonomía: moevec.org la consulta para verificar
  que sus áreas y anclas coinciden.
  """
  use MeeWeb, :controller

  alias Mee.Atlas

  def index(conn, _params) do
    site = Application.get_env(:mee, :moevec_site_url, "https://moevec.org")

    areas =
      for area <- Atlas.list_areas() do
        %{
          slug: area.slug,
          position: area.position,
          name: area.name,
          motto: area.motto,
          applied: area.applied,
          url_red: url(~p"/areas/#{area.slug}"),
          url_sitio: "#{site}/areas/#{area.slug}/",
          subcategories:
            for sub <- area.subcategories do
              %{
                slug: sub.slug,
                position: sub.position,
                name: sub.name,
                summary: sub.summary,
                url_red: url(~p"/areas/#{area.slug}?sub=#{sub.slug}"),
                url_sitio: "#{site}/areas/#{area.slug}/##{sub.slug}"
              }
            end
        }
      end

    conn
    |> put_resp_header("cache-control", "public, max-age=3600")
    |> json(%{version: 1, areas: areas})
  end
end
