import asyncio
import pytest
import websockets


@pytest.mark.asyncio
async def test_websocket_echo():
    uri = "wss://echo.websocket.org"

    async with websockets.connect(uri) as websocket:
        message = "Hello, WebSocket!"
        await websocket.send(message)

        response = await websocket.recv()

        assert response == message, (
            "Ответ должен совпадать с отправленным сообщением"
        )
