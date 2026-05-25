# Sherlock App — Agent Guide

## Overview

Sherlock App is a Cyberpunk-themed OSINT dashboard with two components:

- **Backend** — Python FastAPI service running Sherlock search engine on port `8000`.
- **Frontend** — Vue 3 + Vite SPA served via Nginx on port `80` (mapped to `8080` externally).

Both components are Dockerized and pushed to Docker Hub as separate images.

## Image Tags

| Component | Docker Image |
|-----------|-------------|
| Backend  | `arturoalvarez/sherlock-backend:latest` |
| Frontend | `arturoalvarez/sherlock-frontend:v1.5` |

## Local Build & Push

### Prerequisites

- Docker (with buildx for multi-arch)
- Logged into Docker Hub (`docker login`)

### Backend

```bash
docker build -t arturoalvarez/sherlock-backend:latest ./backend
docker push arturoalvarez/sherlock-backend:latest
```

### Frontend

```bash
docker build -t arturoalvarez/sherlock-frontend:v1.5 ./frontend
docker push arturoalvarez/sherlock-frontend:v1.5
```

### Multi-Arch (ARM64 + AMD64)

```bash
docker buildx build --platform linux/amd64,linux/arm64 \
  -t arturoalvarez/sherlock-backend:latest ./backend --push

docker buildx build --platform linux/amd64,linux/arm64 \
  -t arturoalvarez/sherlock-frontend:v1.5 ./frontend --push
```

## CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/deploy.yml`) automates:

1. **Build** — Builds both backend and frontend Docker images.
2. **Push** — Pushes both images to Docker Hub using `DOCKER_USERNAME` and `DOCKER_TOKEN` secrets.
3. **Trigger** — Runs on every push to `main` branch, or can be triggered manually.

### Secrets Required

Configure these in the GitHub repository settings:

| Secret | Description |
|--------|-------------|
| `DOCKER_USERNAME` | Docker Hub username (`arturoalvarez`) |
| `DOCKER_TOKEN` | Docker Hub access token (or password) |

## Local Development

### Backend

```bash
cd backend
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
pnpm install
pnpm dev
```

### Docker Compose (full stack)

```bash
docker compose up -d --build
```
