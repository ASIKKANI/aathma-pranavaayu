from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scraper import get_air_metrics
import uvicorn
import threading
import time
from contextlib import asynccontextmanager

# Global storage for real-time metrics
cached_metrics = {
    "AQI": "0", "PM1": "0", "PM2.5": "0", "PM4": "0", "PM10": "0",
    "CO2": "0", "TVOC": "0", "NOx": "0", "Temperature": "0", "Humidity": "0"
}

def recursive_scraper():
    """Background task that scrapes the dashboard every 10 seconds."""
    global cached_metrics
    print("Background Scraper Started (Recursive: 10s)")
    while True:
        try:
            start_time = time.time()
            data = get_air_metrics()
            
            # Update cache if we found valid data
            if data and any(v != "0" for v in data.values()):
                cached_metrics = data
                print(f"[{time.strftime('%H:%M:%S')}] SYNC SUCCESS | AQI: {data.get('AQI')} | PM2.5: {data.get('PM2.5')}")
            else:
                print(f"[{time.strftime('%H:%M:%S')}] SYNC PENDING | Dashboard still loading or blocked...")
            
            # Calculate sleep to maintain 10s interval regardless of scrape duration
            elapsed = time.time() - start_time
            sleep_time = max(1, 10 - elapsed)
            time.sleep(sleep_time)
            
        except Exception as e:
            print(f"Scraper Loop Error: {e}")
            time.sleep(10)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Start recursive scraper thread
    thread = threading.Thread(target=recursive_scraper, daemon=True)
    thread.start()
    yield
    # Shutdown: Thread will exit as it's a daemon

app = FastAPI(lifespan=lifespan)

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/metrics")
def get_metrics():
    """Returns the latest cached metrics instantly."""
    return cached_metrics

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
