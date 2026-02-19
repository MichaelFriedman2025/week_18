from mongo_connection import get_mongo_connection


class MongoDal:

    @staticmethod
    def alerts_by_border_and_priority():
        coll = get_mongo_connection()
        pipeline = [{"$project":{"_id":0}},
                    {"$group":{"_id":"$border","$priority":{"$sum":1}}},
                    {"$sort":{"priority":-1}}]
        res = coll.aggregate(pipeline)
        return list(res)
    
    @staticmethod
    def top_urgent_zones():
        coll = get_mongo_connection()
        pipeline = [{"$project":{"_id":0}},
                    {"$match":{"priority":"URGENT"}},
                    {"$group":{"_id":"$zone","count":{"$sum":1}}},
                    {"$sort":{"zone":-1}},
                    {"$limit":5}
                    ]
        res = coll.aggregate(pipeline)
        return list(res)
    
    
    @staticmethod
    def distance_distribution():
        coll = get_mongo_connection()
        pipeline = []
        res = coll.aggregate(pipeline)
        return list(res)
    
    @staticmethod
    def low_visibility_high_activity():
        coll = get_mongo_connection()
        pipeline = []
        res = coll.aggregate(pipeline)
        return list(res)

    @staticmethod
    def hot_zones():
        coll = get_mongo_connection()
        pipeline = []
        res = coll.aggregate(pipeline)
        return list(res)
