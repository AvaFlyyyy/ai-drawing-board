import os
import turtle
from dotenv import load_dotenv
import requests

# 加载密钥
load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    print("❌ 密钥未找到！")
    exit()

# 1. 用户输入
theme = input("🎨 你想画什么？请输入一个词（比如：星空、森林、城堡）：")

# 2. 调用 AI 生成描述
url = "https://api.deepseek.com/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
data = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": f"请用不超过20个字，描述一下‘{theme}’的画面，要包含颜色和形状。"}]
}

response = requests.post(url, headers=headers, json=data)
description = response.json()["choices"][0]["message"]["content"]
print(f"🤖 AI 描述：{description}")

# 3. 海龟画图
t = turtle.Pen()
t.speed(0)
t.pensize(2)

# 根据描述中的关键词选颜色
if "深蓝" in description or "蓝" in description:
    main_color = "darkblue"
else:
    main_color= "blue"
if "银白"in description or "白" in description or "碎钻" in description:
    star_color = "white"
else:
    star_color = "lightgray"

t.pencolor(main_color)
t.fillcolor(main_color)
t.begin_fill()
t.circle(200)
t.end_fill()

t.pencolor(star_color)
t.pensize(3)
for i in range(60):
    t.penup()
    t.goto(0,0)
    t.setheading(i*10)
    t.forward(i*3+10)
    t.pendown()
    t.circle(2)

turtle.done()