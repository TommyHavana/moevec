FROM node:22-alpine AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --no-audit --no-fund
COPY app ./app
COPY lib ./lib
COPY content ./content
COPY public ./public
COPY scripts ./scripts
COPY wordpress ./wordpress
COPY docs ./docs
COPY fuentes ./fuentes
COPY next.config.mjs tsconfig.json ./
RUN npm run build

FROM nginx:1.30-alpine
COPY deploy/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/out /usr/share/nginx/html
