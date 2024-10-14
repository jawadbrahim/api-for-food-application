import redis
from ..config.development import Development
import json

class Rediscache:
    def __init__(self):
        try:
            self.redis_client = redis.StrictRedis(
                host=Development.REDIS_HOST,
                password=Development.REDIS_PASSWORD,
                port=Development.REDIS_PORT,
                decode_responses=True,
                db=0
            )
            if self.redis_client.ping():
                print("Connection successful")
            else:
                print("Connection unsuccessful")
        except redis.ConnectionError as e:
            print(f"Cannot connect to Redis: {str(e)}")
            self.redis_client = None

    def get_cache(self, cache_key):
        if self.redis_client:
            cached_data = self.redis_client.get(cache_key)
            if cached_data:
                return cached_data
        return None

    def set_cache(self, cache_key, data, expired_time=3600):
        if self.redis_client:
            json_data = json.dumps(data, ensure_ascii=False).encode("utf-8")
            return self.redis_client.setex(cache_key, expired_time, json_data)
