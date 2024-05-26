import asyncio

import async_timeout
from fastapi import HTTPException

from src.query.utils import post_processing

GENERATION_TIMEOUT_SEC = 60


async def stream_generator(subscription):
    async with async_timeout.timeout(GENERATION_TIMEOUT_SEC):
        try:
            async for chunk in subscription:
                yield post_processing(chunk)
        except asyncio.TimeoutError:
            raise HTTPException(status_code=504, detail="Stream timed out")
