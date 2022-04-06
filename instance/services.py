"""Services module."""

from aioredis import Redis


class Service:
    def __init__(self, redis: Redis) -> None:
        self._redis = redis

    async def process(self) -> str:
        await self._redis.set("status", "OK")
        return await self._redis.get("status", encoding="utf-8")