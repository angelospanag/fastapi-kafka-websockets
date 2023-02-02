from aiokafka import AIOKafkaConsumer
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.websockets import WebSocket

TOPICS = "quickstart-events"
BOOTSTRAP_SERVERS = "localhost:9092"
GROUP_ID = "my-group"
AUTO_OFFSET_RESET = "latest"

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    consumer = AIOKafkaConsumer(
        TOPICS,
        bootstrap_servers=BOOTSTRAP_SERVERS,
        group_id=GROUP_ID,
        auto_offset_reset=AUTO_OFFSET_RESET,
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
