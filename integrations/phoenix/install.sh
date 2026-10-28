#!/usr/bin/env bash
# Instala la integración con moevec.org sobre el proyecto con Fase 1 y Fase 2.
# Uso: ./install.sh /ruta/al/proyecto/mee
set -euo pipefail

DEST="${1:?Uso: $0 /ruta/al/proyecto/mee}"
SRC="$(cd "$(dirname "$0")" && pwd)"
ROUTER="$DEST/lib/mee_web/router.ex"
ENDPOINT="$DEST/lib/mee_web/endpoint.ex"

[[ -f "$DEST/lib/mee_web/live/home_live.ex" ]] || { echo "Falta la Fase 2"; exit 1; }

cp -r "$SRC/lib/." "$DEST/lib/"
echo "código copiado"

# Migración con timestamp posterior a la última existente
last=$(ls "$DEST/priv/repo/migrations" | grep -oE '^[0-9]{14}' | sort | tail -1)
base=$(date -u +%s)
last_epoch=$(date -u -d "${last:0:8} ${last:8:2}:${last:10:2}:${last:12:2}" +%s)
(( last_epoch >= base )) && base=$((last_epoch + 1))
if ! ls "$DEST/priv/repo/migrations"/*_create_external_articles.exs >/dev/null 2>&1; then
  ts=$(date -u -d "@$base" +%Y%m%d%H%M%S)
  cp "$SRC/migrations/04_create_external_articles.exs" "$DEST/priv/repo/migrations/${ts}_create_external_articles.exs"
  echo "migración: ${ts}_create_external_articles.exs"
fi

# Rutas
if ! grep -q "MEE:api" "$ROUTER"; then
  python3 - "$ROUTER" "$SRC/snippets/router.ex" <<'PY'
import sys
router, snippet = sys.argv[1], sys.argv[2]
src = open(router).read().rstrip()
src = src[:-3].rstrip() + "\n" + open(snippet).read() + "end\n"
open(router, "w").write(src)
PY
  echo "rutas: /api/v1 y /api/webhooks agregadas"
fi

# Cuerpo crudo para verificar firmas
if ! grep -q "CacheBodyReader" "$ENDPOINT"; then
  sed -i 's|    parsers: \[:urlencoded, :multipart, :json\],|    parsers: [:urlencoded, :multipart, :json],\n    body_reader: {MeeWeb.CacheBodyReader, :read_body, []},|' "$ENDPOINT"
  grep -q "CacheBodyReader" "$ENDPOINT" && echo "endpoint: body_reader configurado" \
    || { echo "No pude parchear endpoint.ex; agrega body_reader a Plug.Parsers a mano"; exit 1; }
fi

# Configuración (secreto por variable de entorno)
if ! grep -q "MEE:moevec" "$DEST/config/runtime.exs"; then
  cat >> "$DEST/config/runtime.exs" <<'EOF'

# MEE:moevec — integración con moevec.org
config :mee, :moevec_site_url, System.get_env("MOEVEC_SITE_URL", "https://moevec.org")
config :mee, :moevec_webhook_secret, System.get_env("MOEVEC_WEBHOOK_SECRET")
EOF
  echo "config: runtime.exs lee MOEVEC_WEBHOOK_SECRET y MOEVEC_SITE_URL"
fi

echo "Listo. Ahora: mix ecto.migrate && export MOEVEC_WEBHOOK_SECRET=\$(openssl rand -hex 32) && mix phx.server"
