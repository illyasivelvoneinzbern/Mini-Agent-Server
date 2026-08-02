from app.llm import chat_with_tools,client,chat_stream
from app.tools_registry import (
    tools,
    tool_map
)
import json
def agent(
    user_input,
    max_iterations=5
):

    messages=[
        {
            "role":"user",
            "content":user_input
        }
    ]

    for i in range(max_iterations):

        response = chat_with_tools(
            messages,
            tools
        )


        # 没有工具调用
        if not response.tool_calls:
            return response.content



        tool_call=response.tool_calls[0]


        name=tool_call.function.name


        args=json.loads(
            tool_call.function.arguments
        )


        # 找对应函数

        func = tool_map.get(name)


        if func is None:

            return "工具不存在"


        try:

            result=func(**args)

        except Exception as e:

            result=f"工具执行失败:{e}"



        # 添加assistant消息

        messages.append(
            {
                "role":"assistant",
                "tool_calls":[tool_call]
            }
        )


        # 添加tool结果

        messages.append(
            {
                "role":"tool",
                "tool_call_id":tool_call.id,
                "content":result
            }
        )
    return "达到最大工具调用次数"
def agent_stream(user_input):

    messages=[
        {
            "role":"user",
            "content":user_input
        }
    ]


    response = chat_with_tools(
        messages,
        tools
    )


    if response.tool_calls:

        tool_call=response.tool_calls[0]

        name=tool_call.function.name

        args=json.loads(
            tool_call.function.arguments
        )


        func=tool_map.get(name)


        if func is None:
            yield "工具不存在"
            return


        try:
            result=func(**args)

        except Exception as e:
            result=f"工具执行失败:{e}"


        messages.append(
            {
                "role":"assistant",
                "content":None,
                "tool_calls":[tool_call]
            }
        )


        messages.append(
            {
                "role":"tool",
                "tool_call_id":tool_call.id,
                "content":result
            }
        )


    print("准备进入stream")


    for chunk in chat_stream(messages):

        yield chunk