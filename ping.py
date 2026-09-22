import requests
import time

URL = "https://yaya-bot-console.onrender.com/"
WEBHOOK = "https://discord.com/api/webhooks/1551903083338928221/qRSSxuSxXD2exYv3uHIO1dwLeJrcTB89hAEYJ7SKkLs9pBgaVR2UsGTTDDu2y7NhXr20"

try:
    start = time.time()
    r = requests.get(URL, timeout=30)
    ms = round((time.time() - start) * 1000)

    print(f"HTTP {r.status_code} | {ms} ms")

except Exception as e:
    print(f"連線失敗：{e}")
    raise
