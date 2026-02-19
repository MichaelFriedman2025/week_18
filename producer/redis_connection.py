from redis import Redis
import os
import json

def redis_connection():
    redis_host = os.getenv("REDIS_HOST")
    r = Redis(host=redis_host,decode_responses=True)
    return r

def ingection_to_redis(quque_name,data:dict):
    r = redis_connection()
    r.lpush(quque_name,json.dumps(data))