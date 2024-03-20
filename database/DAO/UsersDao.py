from database.DAO import MongoBaseDao


class UsersDao(MongoBaseDao):
    def __init__(self):
        super().__init__()
        self.collection = "users"

    def insert_user(self, data):
        self.__insert__(data)

    def find_user(self, query):
        return self.__get_one__(query)

    def update_user(self, query, data):
        self.__update__(query, data)

    def delete_user(self, query):
        self.__delete_one__(query)
