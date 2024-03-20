from database.DAO.ProductsDao import ProductsDao


class ProductsEntity:

    def create_product(self, data):
        with ProductsDao() as productsDao:
            productsDao.create_product(data)

    def get_product(self, query):
        with ProductsDao() as productsDao:
            return productsDao.get_product(query)

    def update_product(self, query, data):
        with ProductsDao() as productsDao:
            productsDao.update_product(query, data)

    def delete_product(self, query):
        with ProductsDao() as productsDao:
            productsDao.delete_product(query)

    def get_all_products(self):
        with ProductsDao() as productsDao:
            return productsDao.get_all_products()
