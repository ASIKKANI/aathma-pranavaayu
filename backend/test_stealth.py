from scrapling import StealthyFetcher
import time

fetcher = StealthyFetcher()
fetcher.configure(adaptive=True)
response = fetcher.fetch("https://nippoairvue.live/tvview/yWhemB3q")
# StealthyFetcher is often synchronous and might not wait for JS
# But let's check if it gets anything different
print("Stealthy Text:", response.get_all_text())
