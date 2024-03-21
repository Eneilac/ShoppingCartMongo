from flask import Blueprint, jsonify, request, abort

from entities.Products import ProductsEntity

blueprint = Blueprint("products_page", __name__, url_prefix="/products")


@blueprint.route('/', methods=['GET'], endpoint='get_products')
def get_products():
    prod_ent = ProductsEntity()
    products = prod_ent.get_all_products()
    if len(products) == 0:
        abort(404)
    for product in products:
        product['_id'] = str(product['_id'])
    return jsonify({"products": products})


@blueprint.route('/<product_name>', methods=['GET'], endpoint='get_product')
def get_product(product_name):
    prod_ent = ProductsEntity()
    query = {"name": product_name}
    product = prod_ent.get_product(query)
    if len(product) == 0:
        abort(404)
    product['_id'] = str(product['_id'])
    return jsonify(product)


@blueprint.route('/', methods=['POST'], endpoint='create_product')
def create_product():
    prod_ent = ProductsEntity()
    data = request.json
    prod_ent.create_product(data)
    return jsonify({"message": f"Product {data.get('name')} created"})


@blueprint.route('/<product_name>', methods=['PUT'], endpoint='update_product')
def update_product(product_name):
    prod_ent = ProductsEntity()
    data = request.json
    query = {"name": product_name}
    prod_ent.update_product(query, data)
    return jsonify({"message": "Product updated"})


@blueprint.route('/<product_name>', methods=['DELETE'], endpoint='delete_product')
def delete_product(product_name):
    prod_ent = ProductsEntity()
    query = {"name": product_name}
    prod_ent.delete_product(query)
    return jsonify({"message": "Product deleted"})
