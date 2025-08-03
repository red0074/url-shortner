# TODO: Implement your data models here
# Consider what data structures you'll need for:
# - Storing URL mappings
# - Tracking click counts
# - Managing URL metadata

from threading import Lock
from datetime import datetime

url_store = {}
lock = Lock()

def save_url_mapping(short_code, original_url):
    with lock:
        url_store[short_code] = {
            "original_url": original_url,
            "created_at": datetime.utcnow(),
            "clicks": 0
        }

def get_original_url(short_code):
    with lock:
        return url_store.get(short_code)

def increment_click(short_code):
    with lock:
        if short_code in url_store:
            url_store[short_code]["clicks"] += 1

def get_stats(short_code):
    with lock:
        data = url_store.get(short_code)
        if data:
            return {
                "url": data["original_url"],
                "clicks": data["clicks"],
                "created_at": data["created_at"].isoformat()
            }
        return None
