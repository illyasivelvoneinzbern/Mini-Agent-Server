from app.tools import get_weather
from app.llm import chat


def agent(user_input):

    if "天气" in user_input:

        if "南京" in user_input:
            city="南京"

        elif "北京" in user_input:
            city="北京"

        elif "上海" in user_input:
            city="上海"

        elif "广州" in user_input:
            city="广州"
            
        else:
            city=None

        result=get_weather(city)

        prompt=f"""
        用户问题:
        {user_input}

        工具结果:
        {result}

        请回答用户
        """

        return chat(prompt)


    else:

        return chat(user_input)