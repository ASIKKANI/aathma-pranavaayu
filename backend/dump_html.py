from scrapling import DynamicFetcher
import time

fetcher = DynamicFetcher()
response = fetcher.fetch("https://nippoairvue.live/tvview/yWhemB3q", wait_until="networkidle")
time.sleep(15)
with open("dump.html", "w", encoding="utf-8") as f:
    f.write(response.text)
print("Dumped HTML to dump.html")
print("Text length:", len(response.get_all_text()))
print("Preview:", response.get_all_text()[:500])
