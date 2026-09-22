import requests
from datetime import datetime

URL = "https://yaya-bot-console.onrender.com/"

try:
    r = requests.get(URL, timeout=30)
    print(f"{datetime.now()} 狀態碼：{r.status_code}")
except Exception as e:
    print(f"{datetime.now()} 錯誤：{e}")
    raise
