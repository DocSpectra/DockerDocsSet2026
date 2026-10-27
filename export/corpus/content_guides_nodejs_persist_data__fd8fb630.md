---
title: Add PostgreSQL and verify Todo data persistence
description: Configure the Node.js sample database and check that Todo items persist.
---

## Prerequisites

Complete [sample setup](containerize.md), [Compose configuration](configure-compose.md), [image building](build-images.md), and [startup verification](run.md). For persistent storage and volume lifecycle, see [Volumes](/manuals/engine/storage/volumes.md).

## Add a local database and persist data

The application uses PostgreSQL for data persistence. Add a database service to your Docker Compose configuration.

### Add database service to Docker Compose

If you haven't already created a `compose.yml` file in the previous section, or if you need to add the database service, update your `compose.yml` file to include the PostgreSQL database service:

```yaml
services:
  # ... existing app services ...

  # ========================================
  # PostgreSQL Database Service
  # ========================================
  db:
    image: postgres:18-alpine
    container_name: todoapp-db
    environment:
      POSTGRES_DB: '${POSTGRES_DB:-todoapp}'
      POSTGRES_USER: '${POSTGRES_USER:-todoapp}'
      POSTGRES_PASSWORD: '${POSTGRES_PASSWORD:-todoapp_password}'
    volumes:
      - postgres_data:/var/lib/postgresql
    ports:
      - '${DB_PORT:-5432}:5432'
    restart: unless-stopped
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U ${POSTGRES_USER:-todoapp} -d ${POSTGRES_DB:-todoapp}']
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 5s
    networks:
      - todoapp-network

# ========================================
# Volume Configuration
# ========================================
volumes:
  postgres_data:
    name: todoapp-postgres-data
    driver: local

# ========================================
# Network Configuration
# ========================================
networks:
  todoapp-network:
    name: todoapp-network
    driver: bridge
```

### Update your application service

Make sure your application service in `compose.yml` is configured to connect to the database:

```yaml {hl_lines="18-20,42-44",collapse=true,title=compose.yml}
services:
  app-dev:
    build:
      context: .
      dockerfile: Dockerfile
      target: development
    container_name: todoapp-dev
    ports:
      - '${APP_PORT:-3000}:3000' # API server
      - '${VITE_PORT:-5173}:5173' # Vite dev server
      - '${DEBUG_PORT:-9229}:9229' # Node.js debugger
    environment:
      NODE_ENV: development
      DOCKER_ENV: 'true'
      POSTGRES_HOST: db
      POSTGRES_PORT: 5432
      POSTGRES_DB: todoapp
      POSTGRES_USER: todoapp
      POSTGRES_PASSWORD: '${POSTGRES_PASSWORD:-todoapp_password}'
      ALLOWED_ORIGINS: '${ALLOWED_ORIGINS:-http://localhost:3000,http://localhost:5173}'
    volumes:
      - ./src:/app/src:ro
      - ./package.json:/app/package.json
      - ./vite.config.ts:/app/vite.config.ts:ro
      - ./tailwind.config.js:/app/tailwind.config.js:ro
      - ./postcss.config.js:/app/postcss.config.js:ro
    depends_on:
      db:
        condition: service_healthy
    develop:
      watch:
        - action: sync
          path: ./src
          target: /app/src
          ignore:
            - '**/*.test.*'
            - '**/__tests__/**'
        - action: rebuild
          path: ./package.json
        - action: sync
          path: ./vite.config.ts
          target: /app/vite.config.ts
        - action: sync
          path: ./tailwind.config.js
          target: /app/tailwind.config.js
        - action: sync
          path: ./postcss.config.js
          target: /app/postcss.config.js
    restart: unless-stopped
    networks:
      - todoapp-network

  db:
    image: postgres:18-alpine
    container_name: todoapp-db
    environment:
      POSTGRES_DB: '${POSTGRES_DB:-todoapp}'
      POSTGRES_USER: '${POSTGRES_USER:-todoapp}'
      POSTGRES_PASSWORD: '${POSTGRES_PASSWORD:-todoapp_password}'
    volumes:
      - postgres_data:/var/lib/postgresql
    ports:
      - '${DB_PORT:-5432}:5432'
    restart: unless-stopped
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U ${POSTGRES_USER:-todoapp} -d ${POSTGRES_DB:-todoapp}']
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 5s
    networks:
      - todoapp-network

volumes:
  postgres_data:
    name: todoapp-postgres-data
    driver: local

networks:
  todoapp-network:
    name: todoapp-network
    driver: bridge
```

1. The PostgreSQL database configuration is handled automatically by the application. The database is created and initialized when the application starts, with data persisted using the `postgres_data` volume.

1. Configure your environment by copying the example file:

   ```console
   $ cp .env.example .env
   ```

   Update the `.env` file with your preferred settings:

   ```env
   # Application Configuration
   NODE_ENV=development
   APP_PORT=3000
   VITE_PORT=5173
   DEBUG_PORT=9230

   # Database Configuration
   POSTGRES_HOST=db
   POSTGRES_PORT=5432
   POSTGRES_DB=todoapp
   POSTGRES_USER=todoapp
   POSTGRES_PASSWORD=todoapp_password

   # Security Configuration
   ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
   ```

1. Run the following command to start your application in development mode:

   ```console
   $ docker compose up app-dev --build
   ```

1. Open a browser and verify that the application is running at [http://localhost:5173](http://localhost:5173) for the frontend or [http://localhost:3000](http://localhost:3000) for the API. The React frontend is served by Vite dev server on port 5173, with API calls proxied to the Express server on port 3000.

1. Add some items to the todo list to test data persistence.

1. After adding some items to the todo list, press `CTRL + C` in the terminal to stop your application.

1. Run the application again:
   ```console
   $ docker compose up app-dev
   ```

1. Refresh [http://localhost:5173](http://localhost:5173) in your browser and verify that the todo items persisted, even after the containers were removed and ran again.
