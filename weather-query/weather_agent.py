import os
from dotenv import load_dotenv
import requests

load_dotenv()
key = os.getenv("AMAP_WEATHER_KEY")

if not key:
    print("❌ 错误：未找到高德天气密钥，请在 .env 文件中添加 AMAP_WEATHER_KEY=你的密钥")
    exit()

def get_weather(city):
    """
    调用高德天气 API，查询指定城市的实时天气。
    返回格式：城市名，天气状况，温度°C
    """
    url = "https://restapi.amap.com/v3/weather/weatherInfo"
    params = {
        "key": key,
        "city": city,
        "extensions": "base"
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        if data["status"] == "1" and data["count"] != "0":
            live = data["lives"][0]
            return f"{live['city']}，{live['weather']}，{live['temperature']}°C"
        else:
            return f"查询失败：{data.get('info', '未知错误')}"
    except Exception as e:
        return f"请求出错：{e}"

if __name__ == "__main__":
    city = input("云浮市")
    result = get_weather(city)
    print(result)