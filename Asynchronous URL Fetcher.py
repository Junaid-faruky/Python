import asyncio
import aiohttp

urls = ["https://example.com", "https://httpbin.org/get"]

async def fetch(session, url):
    async with session.get(url) as resp:
        print(f"{url} -> {resp.status}")

async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*(fetch(session, u) for u in urls))

asyncio.run(main())
