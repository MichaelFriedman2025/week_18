

def Priority_Classification_Rules(data:dict):
    if data["weapons_count"] > 0:
        return "URGENT"
    elif data["distance_from_fence_m"] <= 50:
        return "URGENT"
    elif data["people_count"] >= 8:
       return "URGENT"
    elif data["vehicle_type"] == "truck":
        return "URGENT"
    elif  data["distance_from_fence_m"] <= 150 and data["people_count"] >=4:
        return "URGENT"
    elif data["vehicle_type"] == "jeep" and data["people_count"] >= 3:
        return "URGENT"
    else:
        return "NORMAL"