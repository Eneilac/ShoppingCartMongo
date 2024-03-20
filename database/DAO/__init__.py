from database.database import Database


class MongoBaseDao:
    def __init__(self):
        self.__database__ = Database()
        self.collection = None

    def __insert__(self, data):
        self.__database__.__insert__(data, self.collection)

    def __insert_many__(self, data):
        self.__database__.__insert_many__(data, self.collection)

    def __get_one__(self, query):
        return self.__database__.__get_one__(query, self.collection)

    def __get_all__(self):
        return self.__database__.__get_all__(self.collection)

    def __update__(self, query, data):
        self.__database__.__update__(query, data, self.collection)

    def __update_many__(self, query, data):
        self.__database__.__update_many__(query, data, self.collection)

    def __delete_one__(self, query):
        self.__database__.__delete_one__(query, self.collection)

    def __delete_many__(self, query):
        self.__database__.__delete_many__(query, self.collection)

    def __close__(self):
        self.__database__.__close__()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__close__()
