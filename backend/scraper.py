from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import re

def get_air_metrics():
    metrics_keys = ["AQI", "PM1", "PM2.5", "PM4", "PM10", "CO2", "TVOC", "NOx", "Temperature", "Humidity"]
    metrics = {k: "0" for k in metrics_keys}
    
    try:
        with sync_playwright() as p:
            # Add arguments to help Chromium run smoothly in cloud environments
            browser = p.chromium.launch(
                headless=True,
                args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]
            )
            page = browser.new_page()
            
            # Navigate and wait for the network to be idle
            page.goto("https://nippoairvue.live/tvview/yWhemB3q", wait_until="networkidle", timeout=45000)
            
            # Wait for JS to render the dashboard values
            print(f"[{time.strftime('%H:%M:%S')}] Rendering dashboard JS...")
            time.sleep(10)
            
            content = page.content()
            browser.close()
            
            soup = BeautifulSoup(content, 'html.parser')
            all_text = soup.get_text(separator=' ', strip=True)
            
            for key in metrics_keys:
                pattern = rf"{re.escape(key)}\s+([\d\.]+)"
                match = re.search(pattern, all_text, re.IGNORECASE)
                if match:
                    metrics[key] = match.group(1)

        return metrics
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] Scraper Hard Error: {e}")
        return {k: "0" for k in metrics_keys}

if __name__ == "__main__":
    print("Executing Hard-Fix Playwright Scraper...")
    print(get_air_metrics())
