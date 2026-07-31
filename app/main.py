from fastapi import FastAPI
from pydantic import BaseModel
from app.llm import chat
from app.agent import agent
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
def chat_api(req:ChatRequest):

    answer = agent(req.message)

    return {
        "answer":answer
    }