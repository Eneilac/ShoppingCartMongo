from database.DAO import MongoBaseDao


class OrdersDao(MongoBaseDao):
    def __init__(self):
        super().__init__()
        self.collection = "orders"

    def create_order(self, data):
        self.__insert__(data)

    def find_order(self, query):
        return self.__get_one__(query)

    def update_order(self, query, data):
        self.__update__(query, data)

    def delete_order(self, query):
        self.__delete_one__(query)