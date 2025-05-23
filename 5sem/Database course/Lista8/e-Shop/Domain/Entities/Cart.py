class Cart:
    def __init__(self, cart_id, customer_id):
        self.cart_id = cart_id
        self.customer_id = customer_id
        self.items = []

    def add_item(self, cart_item):
        existing_item = next((item for item in self.items if item.product_id == cart_item.product_id), None)
        if existing_item:
            existing_item.quantity += cart_item.quantity
        else:
            self.items.append(cart_item)

    def remove_item(self, product_id):
        self.items = [item for item in self.items if item.product_id != product_id]

    def get_total_price(self):
        return sum(item.quantity * item.price for item in self.items)
