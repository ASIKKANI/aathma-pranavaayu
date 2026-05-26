from scrapling import StealthyFetcher
import json

def test_scrape():
    fetcher = StealthyFetcher()
    # We need to wait for the page to load the metrics
    response = fetcher.get("https://nippoairvue.live/tvview/yWhemB3q")
    
    # Introspect response
    print(f"Response status: {response.status}")
    print(f"Response type: {type(response)}")
    
    # Scrapling response usually has a selector
    page = response.selector
    
    results = {}
    labels = ["AQI", "PM1", "PM2.5", "PM4", "PM10", "CO2", "TVOC", "NOx", "Temperature", "Humidity"]
    
    for label in labels:
        try:
            # Scrapling's Selector uses css or xpath
            # Let's try xpath as suggested by subagent
            element = page.xpath(f"//*[text()='{label}']/following-sibling::*[1]")
            if element:
                results[label] = element[0].text.strip()
            else:
                # Try finding text node if following-sibling doesn't work
                results[label] = "Not found"
        except Exception as e:
            results[label] = f"Error: {str(e)}"
            
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    test_scrape()
