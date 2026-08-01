# Repository Guide

## Structure

- `frontend/` is the Vue 3/Vite/Tailwind app; its entrypoint is `src/main.js` and the main UI is `src/App.vue`.
- `backend/` is the FastAPI app; `app/main.py` serves the API and the compiled frontend, while `app/runner.py` invokes the external `sherlock` executable.
- `GET /search/{username}` is an SSE endpoint. Keep the backend event names (`status`, `match`, `done`, `error`) in sync with `frontend/src/App.vue`.
- `backend/data/` is runtime data mounted by Compose and ignored by Git; do not commit local history or generated files from it.

## Commands

- Use pnpm, not npm: the frontend lockfile and `package.json` pin pnpm 10.12.1. From `frontend/`, run `pnpm install`, `pnpm dev`, `pnpm build`, or `pnpm preview`.
- For local backend work, from `backend/` create/activate the virtualenv, run `pip install -r requirements.txt`, then install `sherlock-project` before `uvicorn app.main:app --reload`; the requirements file does not provide the Sherlock CLI.
- From the repository root, use `docker compose up -d --build`; `backend/Dockerfile` uses the root context and produces one image containing both services on port 8000.
- There are no configured automated tests, lint scripts, typechecks, or formatters. At minimum run `pnpm build` after frontend changes and manually smoke-test backend/API changes.

## Configuration

- `VITE_API_URL` is embedded by Vite at frontend build time. The integrated `backend/Dockerfile` accepts it as `ARG VITE_API_URL`; leave it empty for same-origin deployment.
- Sherlock searches default to `SHERLOCK_TIMEOUT=120` and `SHERLOCK_IGNORE_EXCLUSIONS=true` in Compose; the latter can increase false positives. Override these environment variables when testing another search mode.
- Backend CORS origins are hard-coded in `backend/app/main.py` for local development and the deployed frontend hostname. Update `ALLOWED_ORIGINS` when the frontend origin changes.
- `.github/workflows/deploy.yml` builds and pushes the integrated image on pushes to `main`; it requires `DOCKER_USERNAME` and `DOCKER_TOKEN` secrets.
