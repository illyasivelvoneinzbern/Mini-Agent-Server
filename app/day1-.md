Fastapi调用：用户http请求router定位pydantic验证api()调用llm.py返回json
llm调用：http请求main到llm
1. FastAPI请求流程
HTTP Request

↓

FastAPI

↓

chat_api()

↓

agent()

↓

LLM

↓

tool

↓

LLM

↓

JSON Response
2. 为什么拆llm.py
3. LLM调用流程
4. LLM App和Agent区别
5. 五段核心代码(get,post,pydantic封装，构建结构体，项目结构)
agent loop结构
Function Calling让LLM输出结构化的工具调用请求，由程序执行具体函数，而不是让LLM直接生成所有答案。
Function Calling 中工具结果如何返回给模型？
模型返回 tool_call 后，程序执行对应函数，然后把执行结果以 role=tool 的消息加入 conversation history，并通过 tool_call_id 关联对应的工具调用，最后再次请求模型生成最终回答。
Agent 如何支持多个工具？
我通过 tool registry 保存工具名和函数映射，LLM 返回 function name 后动态路由执行。
调用工具循环次数需限制，调用不到需要反馈
agent loop:
用户请求进入FastAPI，然后Agent调用LLM判断是否需要工具。如果LLM返回tool_call，则解析参数，通过tool_registry找到对应函数执行，再把tool结果加入messages继续调用LLM，直到生成最终答案。
在实现 Agent streaming 时，遇到了 Python generator 嵌套问题。由于 StreamingResponse 需要消费外层 iterator，直接 return 内层 generator 会导致数据无法正确透传，因此改为遍历内部 generator 并逐chunk yield。