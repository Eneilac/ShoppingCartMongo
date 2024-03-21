from pymongo import MongoClient

from constants import DATABASE_NAME, DB_USER, DB_PASSWORD, CLUSTER_NAME

db_user = DB_USER
password = DB_PASSWORD
cluster_name = CLUSTER_NAME
db_name = DATABASE_NAME

uri = f"mongodb+srv://{db_user}:{password}@pit-plus.jgz6izo.mongodb.net/?retryWrites=true&w=majority&appName={cluster_name}"


class Database:
    def __init__(self):
        self.__client__ = MongoClient(uri)
        self.__db__ = self.__client__[db_name]

    def __get_collection__(self, collection):
        return self.__db__[collection]

    def __insert__(self, data, collection):
        self.__db__[collection].insert_one(data)

    def __insert_many__(self, data, collection):
        self.__db__[collection].insert_many(data)

    def __get_one__(self, query, collection):
        return self.__db__[collection].find_one(query)

    def __get_all__(self, collection):
        cursor = self.__db__[collection].find({})
        lst = []
        for document in cursor:
            lst.append(document)
        return lst

    def __update__(self, query, data, collection):
        self.__db__[collection].update_one(query, {"$set": data})

    def __update_many__(self, query, data, collection):
        self.__db__[collection].update_many(query, data)

    def __delete_one__(self, query, collection):
        self.__db__[collection].delete_one(query)

    def __delete_many__(self, query, collection):
        self.__db__[collection].delete_many(query)

    def __close__(self):
        self.__client__.close()
