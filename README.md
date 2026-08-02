# Mini Agent Server


## 项目介绍

一个基于 FastAPI + DeepSeek API
实现的轻量级 Agent 后端。

支持：

- Function Calling
- Tool Execution
- Multi Tool Routing
- Streaming Response


---

## Architecture


User

↓

FastAPI

↓

Agent Loop

↓

LLM

↓

Tool Registry

↓

Tools


---

## Tech Stack

Backend:
- FastAPI

LLM:
- DeepSeek API

Agent:
- Function Calling

Tools:
- Weather
- Calculator


---

## Project Structure


app/

├── main.py

├── agent.py

├── llm.py

├── tools.py

├── tools_registry.py

└── schemas.py


---

## Run


1. install


pip install -r requirements.txt


2. config


.env


DEEPSEEK_API_KEY=xxx


3. start


uvicorn app.main:app --reload



---

## API


POST /chat


Request:

{
 "message":"北京天气怎么样"
}


Response:

{
 "answer":"北京晴天30℃"
}



---

## Design


Agent Loop:


User

↓

LLM reasoning

↓

Tool Calling

↓

Tool Execution

↓

Final Answer



---

## Future Improvement


- Memory
- RAG
- LangGraph workflow
- Docker deployment
