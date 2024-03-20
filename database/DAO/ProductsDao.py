from database.DAO import MongoBaseDao


class ProductsDao(MongoBaseDao):
    def __init__(self):
        super().__init__()
        self.collection = "products"

    def create_product(self, data):
        self.__insert__(data)

    def create_many_products(self, data):
        self.__insert_many__(data)

    def get_product(self, query):
        return self.__get_one__(query)

    def get_all_products(self, ):
        return self.__get_all__()

    def update_product(self, query, data):
        self.__update__(query, data)

    def update_many_products(self, query, data):
        self.__update_many__(query, data)

    def delete_product(self, query):
        self.__delete_one__(query)

    def delete_many_products(self, query):
        self.__delete_many__(query)
