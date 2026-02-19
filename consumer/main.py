from redis_connection import get_redis_connection
from mongo_connection import get_mongo_connection
import datetime
import json

r = get_redis_connection()
coll = get_mongo_connection() 
try:
    while True:
        doc = r.rpop("urgent_queue")
        if doc == None:
            doc = r.rpop("normal_queue")
            if doc == None:
                continue
        new_doc = json.loads(doc)
        new_doc["insertion_time"] = str(datetime.datetime.now())
        
        # coll.insert_one(new_doc)
        

except Exception as error:
    print("error:",error)
            


