# CyberOSINT Sherlock Dashboard

A modern, Cyberpunk-themed OSINT dashboard for the Sherlock search engine.

## Tech Stack
- **Frontend**: Vue 3 (Composition API), Vite, Tailwind CSS, pnpm.
- **Backend**: FastAPI, Sherlock.
- **Database**: Local JSON history.
- **Deployment**: Docker (ARM64 supported).

## Local Development

### Backend
1. `cd backend`
2. `python3 -m venv venv && source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `pip install sherlock-project`
5. `uvicorn app.main:app --reload`

### Frontend
1. `cd frontend`
2. `pnpm install`
3. `pnpm dev`

### Search Configuration

The container runs Sherlock in exhaustive mode by default:

- `SHERLOCK_TIMEOUT=120`: maximum seconds to wait for each site response.
- `SHERLOCK_IGNORE_EXCLUSIONS=true`: also checks sites excluded by Sherlock upstream; this can produce more false positives.
- NSFW checks remain enabled through the fixed `--nsfw` option.

Override these values when starting Compose if needed:

```bash
SHERLOCK_TIMEOUT=180 SHERLOCK_IGNORE_EXCLUSIONS=false docker-compose up -d --build
```

## Docker Deployment (ARM64)

To build and push the single application image for ARM64 architecture (e.g., for Raspberry Pi or Apple Silicon servers):

```bash
docker buildx build --platform linux/arm64 -f backend/Dockerfile -t your-dockerhub-user/sherlock-app:latest . --push
```

### Docker Compose
```bash
docker-compose up -d --build
```

The container serves the Vue application and FastAPI from the same origin on port `8000`.
Expose it through one subdomain (for example, `sherlock.example.com`) using the reverse proxy or TLS terminator on the host.
For the local Compose test, open `http://localhost:8080`.

## Git Initialization

```bash
git init
git add .
git commit -m "feat: initial commit - cyberpunk osint dashboard"
git remote add origin https://github.com/your-user/sherlock-app.git
git branch -M main
git push -u origin main
```

## Security & OSINT
This tool is for educational and authorized research purposes only. Always respect privacy and terms of service of the targeted platforms.
