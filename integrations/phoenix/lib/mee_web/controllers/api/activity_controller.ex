defmodule MeeWeb.Api.ActivityController do
  @moduledoc """
  GET /api/v1/areas/:slug/posts?sub=<slug>&limit=<1..20>

  Publicaciones recientes de un área (o de una subcategoría) para que
  moevec.org muestre "La conversación en la red" en cada página de área.
  Solo devuelve datos públicos: nunca correos ni ids de usuario.
  """
  use MeeWeb, :controller

  alias Mee.{Atlas, Content}

  @max_limit 20

  def index(conn, %{"slug" => slug} = params) do
    case Enum.find(Atlas.list_areas(), &(&1.slug == slug)) do
      nil ->
        conn |> put_status(404) |> json(%{error: "área desconocida"})

      area ->
        sub = Enum.find(area.subcategories, &(&1.slug == params["sub"]))
        limit = parse_limit(params["limit"])

        posts =
          Content.list_posts([area_id: area.id, subcategory_id: sub && sub.id], limit: limit)

        conn
        |> put_resp_header("cache-control", "public, max-age=60")
        |> json(%{
          area: area.slug,
          subcategory: sub && sub.slug,
          posts: Enum.map(posts, &serialize/1)
        })
    end
  end

  defp parse_limit(value) do
    case Integer.parse(to_string(value || "")) do
      {n, ""} when n in 1..@max_limit -> n
      _ -> 5
    end
  end

  defp serialize(post) do
    %{
      id: post.id,
      title: post.title,
      excerpt: post.body |> String.slice(0, 280),
      level: post.level,
      subcategory: post.subcategory.slug,
      author:
        post.author && %{handle: post.author.handle, display_name: post.author.display_name},
      url: url(~p"/p/#{post.id}"),
      published_at: post.inserted_at
    }
  end
end
