
  # MEE:api — integración con moevec.org
  pipeline :moevec_webhook do
    plug :accepts, ["json"]
    plug MeeWeb.Plugs.VerifyWebhook
  end

  scope "/api/v1", MeeWeb.Api do
    pipe_through :api

    get "/areas", AtlasController, :index
    get "/areas/:slug/posts", ActivityController, :index
  end

  scope "/api/webhooks", MeeWeb.Api do
    pipe_through :moevec_webhook

    post "/moevec", WordpressWebhookController, :create
  end
  # MEE:api:end
