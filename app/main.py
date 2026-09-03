import asyncio

from fastapi import FastAPI


app = FastAPI(title="HireOps")

JOBS = []
CANDIDATES = []


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/ready")
async def ready():
    # TODO: check Postgres and Redis (D3)
    return {"status": "ready", "checks": {}}


@app.get("/jobs")
async def jobs():
    return JOBS


@app.get("/candidates")
async def candidates():
    return CANDIDATES


@app.get("/slow")
async def slow():
    await asyncio.sleep(5)
    return {"status": "ok"}

