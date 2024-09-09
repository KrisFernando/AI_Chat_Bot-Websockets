import websockets
import asyncio
import json

PORT = 3001
print(f'Server is listening on port: {PORT}')

async def echo(websocket):
    print('A Client just connected!')
    async for payload in websocket:
        message = json.loads(payload)["message"]
        print(message)
        await websocket.send(message)

async def main():
    async with websockets.serve(echo, "localhost", PORT):
        await asyncio.Future()  # run forever

asyncio.run(main())