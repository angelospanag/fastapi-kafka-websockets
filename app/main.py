from aiokafka import AIOKafkaConsumer
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.websockets import WebSocket

from app.config import get_settings

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    consumer = AIOKafkaConsumer(
        get_settings().topics,
        bootstrap_servers=get_settings().bootstrap_servers,
        group_id=get_settings().group_id,
        auto_offset_reset=get_settings().auto_offset_reset,
    )
    await websocket.accept()
    while True:
        await consumer.start()
        try:
            async for msg in consumer:
                print(
                    "consumed: ",
                    msg.topic,
                    msg.partition,
                    msg.offset,
                    msg.key,
                    msg.value,
                    msg.timestamp,
                )
                await websocket.send_text(msg.value.decode("utf-8"))
        finally:
            await consumer.stop()
