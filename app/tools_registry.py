from app.tools import (
    get_weather,
    calculator,
    weather_tool,
    calculator_tool
)


tools = [
    weather_tool,
    calculator_tool
]


tool_map = {

    "get_weather": get_weather,

    "calculator": calculator

}