def get_weather(city:str):

    weather_data = {
        "北京":"晴天，30℃",
        "上海":"小雨，25℃",
        "广州":"多云，32℃"
    }

    return weather_data.get(
        city,
        "暂无天气信息"
    )
weather_tool = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "查询指定城市天气",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "城市名称"
                }
            },
            "required": ["city"]
        }
    }
}
def calculator(a,b,operator):

    if operator=="+":
        return a+b

    if operator=="-":
        return a-b

    if operator=="*":
        return a*b
calculator_tool={
"type":"function",
"function":{
"name":"calculator",
"description":"数学计算",
"parameters":{
"type":"object",
"properties":{
"a":{
"type":"number"
},
"b":{
"type":"number"
},
"operator":{
"type":"string"
}
},
"required":[
"a",
"b",
"operator"
]
}
}
}
