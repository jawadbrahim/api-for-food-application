import redis
from ..config.development import Development
import json

try: 
    redis_client = redis.StrictRedis(
        host=Development.REDIS_HOST,
        password=Development.REDIS_PASSWORD,
        port=Development.REDIS_PORT,
        decode_responses=True,
        db=0
    )
    if redis_client.ping():
        print("Connection successfully")
    else:
        print("Connection unsuccessfully")
except redis.ConnectionError as e:
    print(f"Cannot connect to redis: {str(e)}")
    redis_client = None

def get_cache(cache_key):
    if redis_client:
        cached_data = redis_client.get(cache_key)
        if cached_data:
            return cached_data
    return None
    
def set_cache(cache_key, data, expired_time=3600):
    if redis_client:
        json_data = json.dumps(data, ensure_ascii=False).encode("utf-8")
        return redis_client.setex(cache_key, expired_time, json_data)
