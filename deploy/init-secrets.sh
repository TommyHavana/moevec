#!/bin/sh
set -eu
mkdir -p /run/mee-secrets
for name in database_password root_password admin_password; do
  path="/run/mee-secrets/$name"
  if [ ! -s "$path" ]; then
    head -c 48 /dev/urandom | base64 | tr -d '\n' > "$path"
    chmod 0644 "$path"
  fi
done
