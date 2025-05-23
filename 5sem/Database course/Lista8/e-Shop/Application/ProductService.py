from ..Domain.Entities import Product
from ..Domain.Repositories import ProductRepository

class ProductService:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    def get_product_by_id(self, product_id):
        return self.product_repository.get_by_id(product_id)

    def get_all_products(self):
        return self.product_repository.get_all()

    def add_product(self, product):
        self.product_repository.add(product)

    def update_product(self, product):
        self.product_repository.update(product)

    def delete_product(self, product_id):
        self.product_repository.delete(product_id)
