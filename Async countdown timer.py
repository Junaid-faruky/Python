# 10. Async countdown timer
import asyncio
async def countdown(n):
    while n:
        print(n)
        await asyncio.sleep(1)
        n -= 1
asyncio.run(countdown(5))
