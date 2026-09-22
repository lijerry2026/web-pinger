import requests
from datetime import datetime

URL = "https://yaya-bot-console.onrender.com/"
WEBHOOK = "https://discord.com/api/webhooks/1551903083338928221/qRSSxuSxXD2exYv3uHIO1dwLeJrcTB89hAEYJ7SKkLs9pBgaVR2UsGTTDDu2y7NhXr20"

try:
    r = requests.get(URL, timeout=30)
    if r.status_code != 200:
        requests.post(WEBHOOK, json={"content": f"⚠️ 網站異常：{r.status_code}"})
except Exception as e:
    requests.post(WEBHOOK, json={"content": f"❌ 網站無法連線：{e}"})
    raise
