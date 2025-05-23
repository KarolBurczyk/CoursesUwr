class Price:
    def __init__(self, amount: float):
        self.amount = amount

    def __repr__(self):
        return f"Price({self.amount})"


class Adress:
    def __init__(self, street: str, city: str, zip_code: str):
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def __repr__(self):
        return f"Adress({self.street}, {self.city}, {self.zip_code})"
