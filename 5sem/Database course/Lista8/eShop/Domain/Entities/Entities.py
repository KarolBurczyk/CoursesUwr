from typing import List, Optional
from uuid import uuid4


class Product:
    def __init__(self, name: str, description: str, price: float, stock: int):
        self.id = uuid4()
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def update_stock(self, quantity: int):
        if self.stock >= quantity:
            self.stock -= quantity

        else:
            raise ValueError("Not enough stock available")

    def __repr__(self):
        return f"Product({self.name}, {self.price}, stock: {self.stock})"


class Cart:
    def __init__(self):
        self.id = uuid4()
        self.items = []

    def add_product(self, product: Product, quantity: int):
        self.items.append({"product": product, "quantity": quantity})

    def remove_product(self, product: Product):
        self.items = [item for item in self.items if item["product"] != product]

    def get_total(self) -> float:
        return sum(item["product"].price * item["quantity"] for item in self.items)

    def __repr__(self):
        return f"Cart({self.id}, {self.items})"


class Order:
    def __init__(self, cart: Cart, adress: str):
        self.id = uuid4()
        self.cart = cart
        self.adress = adress
        self.status = "Created"

    def pay(self):
        if self.status == "Created":
            self.status = "Paid"
        else:
            raise ValueError("Order already paid")

    def ship(self):
        if self.status == "Paid":
            self.status = "Shipped"
        else:
            return ValueError("Order cannot be shipped unless paid")

    def __repr__(self):
        return f"Order({self.id}, {self.cart}, {self.adress}, {self.status})"
