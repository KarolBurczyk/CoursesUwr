class Product:
    def __init__(self, product_id, name, description, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock_quantity = stock_quantity

    def add_to_stock(self, quantity):
        self.stock_quantity += quantity

    def remove_from_stock(self, quantity):
        if quantity > self.stock_quantity:
            raise ValueError("Not enough stock")
        self.stock_quantity -= quantity

    def update_price(self, new_price):
        self.price = new_price

