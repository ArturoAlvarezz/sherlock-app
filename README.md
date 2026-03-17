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
4. `uvicorn app.main:app --reload`

### Frontend
1. `cd frontend`
2. `pnpm install`
3. `pnpm dev`

## Docker Deployment (ARM64)

To build and push images for ARM64 architecture (e.g., for Raspberry Pi or Apple Silicon servers):

```bash
# Backend
docker buildx build --platform linux/arm64 -t your-dockerhub-user/sherlock-backend:latest ./backend --push

# Frontend
docker buildx build --platform linux/arm64 -t your-dockerhub-user/sherlock-frontend:latest ./frontend --push
```

### Docker Compose
```bash
docker-compose up -d --build
```

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
