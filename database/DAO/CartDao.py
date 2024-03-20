from database.DAO import MongoBaseDao


class CartDao(MongoBaseDao):
    def __init__(self):
        super().__init__()
        self.collection = "cart"

    def create_cart(self, data):
        self.__insert__(data)

    def find_cart(self, query):
        return self.__get_one__(query)

    def update_cart(self, query, data):
        self.__update__(query, data)

    def delete_cart(self, query):
        self.__delete_one__(query)

    def add_product(self, query, data):
        self.__update__(query, data)