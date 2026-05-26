from scrapling import StealthyFetcher
import time

fetcher = StealthyFetcher()
response = fetcher.fetch("https://nippoairvue.live/tvview/yWhemB3q")
time.sleep(10) # Heavy wait
print("PAGE TEXT CONTENT:")
print(response.get_all_text())
print("-" * 20)
print("LABELS FOUND:")
for label in ["AQI", "PM1", "PM2.5", "PM10", "CO2"]:
    found = response.xpath(f"//*[contains(text(), '{label}')]")
    print(f"{label}: {'Found' if found else 'NOT FOUND'}")
