import requests

url = "https://www.googleapis.com/customsearch/v1"
params = {
    "key": "AIzaSyDtmm_Zxksek83JssFBfT1XU9BJabHDqn0" ,
    "cx": "7531d2c0fc28f483c",
    "q": "Model Context Protocol MCP"
}

response = requests.get(url, params=params)
print(response.json())