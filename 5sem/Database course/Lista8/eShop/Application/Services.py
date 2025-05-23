from ..Domain.Repositories import ProductRepository, CartRepository, OrderRepository

class ProductService:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    def get_all_products(self):
        # for now:
        return [
            {
                "id": 1,
                "name": "Dog food",
                "price": 100,
                "description": "High noutrition canned beef for dogs",
            },
            {
                "id": 2,
                "name": "AirPods",
                "price": 800,
                "description": "New model of world wide known Apple headphones",
            },
        ]

    def get_product_details(self, product_id):
        # for now:
        return {
            "id": product_id,
            "name": "Neckless",
            "price": 4000,
            "description": "Silver neckless with diamonds, perfect for an evening date",
        }

    def create_product(self, name, price, description):
        new_product = Product(name=name, price=price, description=description)
        self.product_repository.save(new_product)
        return new_product

    def update_product(self, product_id, name, price, description):
        product = self.product_repository.get_by_id(product_id)
        if not product:
            raise ValueError("Product not found")
        product.name = name
        product.price = price
        product.description = description
        self.product_repository.save(product)

    def delete_product(self, product_id):
        self.product_repository.delete(product_id)


class CartService:
    def __init__(self, cart_repository):
        self.cart_repository = cart_repository

    def get_cart_content(self, cart_id):
        # for now:
        return {
            "cart_id": cart_id,
            "products": [
                {"id": 0, "name": "Dog Food", "price": 100, "quantity": 3},
                {"id": 1, "name": "AirPods", "price": 800, "quantity": 1},
                {"id": 2, "name": "Neckless", "price": 4000, "quantity": 1},
            ],
        }

    def add_product_to_cart(self, cart_id, product_id, quantity):
        cart = self.cart_repository.get_by_id(cart_id)
        if not cart:
            raise ValueError("Cart not found")
        cart.add_product(product_id, quantity)
        self.cart_repository.save(cart)

    def remove_product_from_cart(self, cart_id, product_id):
        cart = self.cart_repository.get_by_id(cart_id)
        if not cart:
            raise ValueError("Cart not found")
        cart.remove_product(product_id)
        self.cart_repository.save(cart)


class OrderService:
    def __init__(self, order_repository):
        self.order_repository = order_repository

    def create_order(self, cart_id, address):
        # for now:
        order = {
            "order_id": 0,
            "cart_id": cart_id,
            "address": address,
            "status": "Created",
        }
        self.order_repository.save(order)
        return order

    def get_order_details(self, order_id):
        return {"order_id": order_id, "status": "Created", "address": "Wrocławska"}

product_service = ProductService(ProductRepository())
product_service.get_all_products()