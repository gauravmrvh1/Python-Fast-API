import redis
import json
import config.redis as redisSettings
from config.redis import REDIS_HOST, REDIS_PORT

class RedisClient:
    def __init__(self):
        self.client = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=redisSettings.REDIS_DB,
            decode_responses=True
        )

    def get(self, key: str):
        value = self.client.get(key)
        return json.loads(value) if value else None

    def set(self, key: str, value, ttl: int = 60):
        self.client.setex(key, ttl, json.dumps(value))

    def delete(self, key: str):
        self.client.delete(key)


redis_client = RedisClient()
