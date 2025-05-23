from ..Domain.Entities import Cart
from ..Domain.Repositories import CartRepository

class CartService:
    def __init__(self, cart_repository):
        self.cart_repository = cart_repository

    def get_cart_by_customer_id(self, customer_id):
        return self.cart_repository.get_by_customer_id(customer_id)

    def add_item_to_cart(self, customer_id, cart_item):
        cart = self.get_cart_by_customer_id(customer_id)
        if not cart:
            cart = Cart(cart_id=len(self.cart_repository.carts) + 1, customer_id=customer_id)
            self.cart_repository.add(cart)
        cart.add_item(cart_item)
        self.cart_repository.update(cart)

    def remove_item_from_cart(self, customer_id, product_id):
        cart = self.get_cart_by_customer_id(customer_id)
        if cart:
            cart.remove_item(product_id)
            self.cart_repository.update(cart)
