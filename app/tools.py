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