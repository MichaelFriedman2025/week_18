from redis import Redis
import os

def get_redis_connection():
    redis_host = os.getenv("REDIS_HOST")
    r = Redis(host=redis_host,decode_responses=True)
    return r


    