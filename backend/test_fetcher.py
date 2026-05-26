from scrapling import DynamicFetcher
import time

def test_dynamic():
    print("Testing DynamicFetcher...")
    try:
        fetcher = DynamicFetcher()
        response = fetcher.fetch("https://nippoairvue.live/tvview/yWhemB3q", wait_until="networkidle", timeout=30000)
        time.sleep(10) # Wait more
        print("Text preview:")
        print(response.text[:500])
        print("...")
        if "AQI" in response.text:
            print("AQI string found in text!")
        else:
            print("AQI string NOT found!")
    except Exception as e:
        print(f"DynamicFetcher Error: {e}")

if __name__ == "__main__":
    test_dynamic()
