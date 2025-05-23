from Domain.Entities import Cart
from Domain.Repositories import CartRepository

class InMemoryCartRepository(CartRepository):
    def __init__(self):
        self.carts = []

    def get_by_customer_id(self, customer_id):
        return next((c for c in self.carts if c.customer_id == customer_id), None)

    def add(self, cart):
        self.carts.append(cart)

    def update(self, cart):
        existing_cart = self.get_by_customer_id(cart.customer_id)
        if existing_cart:
            self.delete(cart.cart_id)
            self.add(cart)

    def delete(self, cart_id):
        self.carts = [c for c in self.carts if c.cart_id != cart_id]
