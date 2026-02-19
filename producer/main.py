from pydantic import BaseModel
from typing import Literal,Optional
from priority_logic import Priority_Classification_Rules
from redis_connection import ingection_to_redis
import json

class Alert(BaseModel):
    border: Optional[Literal["jordan","syria","gaza","lebanon","egypt"]]
    zone: str
    timestamp:str
    people_count:int
    weapons_count:int
    vehicle_type:str
    distance_from_fence_m:int
    visibility_quality:float



try:
    with open("border_alerts.json","r",encoding="utf-8") as f:
        data = json.load(f)
except Exception:
    print("error: not found the file")

try:
    for doc in data:
        Alert(**doc)
        priority = Priority_Classification_Rules(doc)
        if priority == "URGENT":
            doc["priority"] = "URGENT"
            ingection_to_redis("urgent_queue",doc)
        elif priority == "NORMAL":
            doc["priority"] = "NORMAL"
            ingection_to_redis("normal_queue",doc)

except Exception as error:
    print("ERROR:",error)