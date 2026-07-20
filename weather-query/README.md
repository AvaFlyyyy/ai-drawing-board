# ☀️ 天气查询工具

这是一个用 Python 写的小工具，可以查询任意中国城市（含县级市）的实时天气，包括天气状况和温度。

## ✨ 功能特点
- 输入城市名（如：北京、云浮市、深圳）
- 返回当前天气状况和温度
- 代码清晰，包含环境变量管理和错误处理

## 🛠️ 技术栈
- Python 3.x
- 高德地图天气 API
- requests + python-dotenv

## 🚀 如何运行
1. 在项目根目录创建 `.env` 文件，填入你的高德 API Key：
   `AMAP_WEATHER_KEY=你的密钥`
2. 安装依赖：`pip install requests python-dotenv`
3. 运行程序：`python weather_agent.py`

## 📸 运行效果
输入 `云浮市` → 输出 `云浮市，阴，26°C`