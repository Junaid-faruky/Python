import asyncio
import websockets

async def chat():
    uri = "wss://echo.websocket.org"
    async with websockets.connect(uri) as ws:
        await ws.send("Hello over WebSocket")
        resp = await ws.recv()
        print("Received:", resp)

asyncio.run(chat())
