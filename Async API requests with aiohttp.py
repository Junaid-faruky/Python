# 1. Async API requests with aiohttp
import aiohttp, asyncio

async def fetch():
    async with aiohttp.ClientSession() as s:
        async with s.get("https://api.github.com") as r:
            print(await r.json())

asyncio.run(fetch())
