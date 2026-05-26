import urllib.request
import json
import time

def get_air_metrics():
    metrics_keys = ["AQI", "PM1", "PM2.5", "PM4", "PM10", "CO2", "TVOC", "NOx", "Temperature", "Humidity"]
    metrics = {k: "0" for k in metrics_keys}
    
    url = "https://nippoairvue.live/api/dashsvc/tvview"
    
    # Send a tiny POST request to the hidden API directly! (Instant & zero heavy browsers needed)
    req = urllib.request.Request(url, method="POST")
    req.add_header("x-auth-key", "yWhemB3q")
    req.add_header("Content-Type", "application/json")
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            p_vals = data.get("data", {}).get("pollutantValues", {}).get("pollutantValues", {})
            
            if p_vals:
                metrics["AQI"] = str(p_vals.get("aqi", {}).get("value", "0"))
                metrics["PM1"] = str(p_vals.get("PM1", {}).get("value", "0"))
                metrics["PM2.5"] = str(p_vals.get("PM2.5", {}).get("value", "0"))
                metrics["PM4"] = str(p_vals.get("PM4", {}).get("value", "0"))
                metrics["PM10"] = str(p_vals.get("PM10", {}).get("value", "0"))
                metrics["CO2"] = str(p_vals.get("CO2", {}).get("value", "0"))
                metrics["TVOC"] = str(p_vals.get("TVOC", {}).get("value", "0"))
                metrics["NOx"] = str(p_vals.get("NOx", {}).get("value", "0"))
                metrics["Temperature"] = str(p_vals.get("TEMPERATURE", {}).get("value", "0"))
                metrics["Humidity"] = str(p_vals.get("HUMIDITY", {}).get("value", "0"))

        return metrics
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] Scraper Hard Error: {e}")
        return {k: "0" for k in metrics_keys}

if __name__ == "__main__":
    print("Executing Lightning-Fast API Scraper...")
    print(get_air_metrics())
