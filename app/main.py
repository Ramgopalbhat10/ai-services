from fastapi import FastAPI, APIRouter
from fastapi.logger import logger
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache.coder import JsonCoder
import logging
from .routers import embedding

app = FastAPI()


logger = logging.getLogger("gunicorn.error")


@app.on_event("startup")
async def startup_event():
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache", coder=JsonCoder)


app.include_router(embedding.router)


@app.get("/status")
async def status():
    return {"status": "ok"}