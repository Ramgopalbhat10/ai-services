from fastapi import APIRouter
from fastapi.logger import logger
from fastapi_cache.decorator import cache
import numpy as np
import logging
from ..utils import load_embedding_model

model = load_embedding_model()
router = APIRouter(
    prefix="/embedding",
    tags=["embedding"]
)

@router.get("")
@cache(expire=6000)
async def get_embedding(text: str):
    logging.info(f"Received text: {text}")
    logger.info(f"Received text: {text}")
    embedding = model.encode(text)
    return {"embedding": np.asarray(embedding).tolist()}