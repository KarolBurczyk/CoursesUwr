from Domain.Entities import Product
from Domain.Repositories import ProductRepository

class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        self.products = []

    def get_by_id(self, product_id):
        return next((p for p in self.products if p.product_id == product_id), None)

    def get_all(self):
        return self.products

    def add(self, product):
        self.products.append(product)

    def update(self, product):
        existing_product = self.get_by_id(product.product_id)
        if existing_product:
            self.delete(product.product_id)
            self.add(product)

    def delete(self, product_id):
        self.products = [p for p in self.products if p.product_id != product_id]
