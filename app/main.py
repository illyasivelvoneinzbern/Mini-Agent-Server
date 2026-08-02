from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import agent,agent_stream
from fastapi.responses import StreamingResponse
app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {
        "message": "Mini Agent Server Running"
    }


@app.get("/hello")
def hello():
    return {
        "msg": "hello"
    }


@app.post("/chat")
async def chat_api(req:ChatRequest):

    answer = agent(req.message)

    return {
        "answer":answer
    }
@app.post("/stream")
def stream(req:ChatRequest):

    return StreamingResponse(
        agent_stream(req.message),
        media_type="text/plain"
    )