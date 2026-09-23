import json
import asyncio
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse
from fastapi.staticfiles import StaticFiles
from app.runner import run_sherlock

app = FastAPI(title="Cyberpunk Sherlock OSINT API")

# Configure CORS for the frontend URL
ALLOWED_ORIGINS = [
    "https://sherlock.arturoalvarez.dev",
    "http://localhost:5173", # For local development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
async def root():
    return {"status": "online", "message": "Cyberpunk OSINT Engine Ready"}



@app.get("/search/{username}")
async def search_username(request: Request, username: str):
    """
    Streams search results as SSE for the given username.
    """
    async def event_generator():
        results = []
        try:
            # Yield 'searching' state
            yield {"event": "status", "data": "Searching..."}
            
            async for found in run_sherlock(username):
                # Check for client disconnection
                if await request.is_disconnected():
                    break
                
                results.append(found)
                # Stream found result
                yield {"event": "match", "data": json.dumps(found)}

            # Finalize search
            if not await request.is_disconnected():
                yield {"event": "done", "data": "Search complete"}

        except Exception as e:
            yield {"event": "error", "data": str(e)}

    return EventSourceResponse(event_generator())


frontend_dist = Path(__file__).resolve().parents[1] / "frontend"
if frontend_dist.is_dir():
    app.mount("/", StaticFiles(directory=frontend_dist, html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
