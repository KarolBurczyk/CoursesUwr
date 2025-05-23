from abc import ABC, abstractmethod

class CartRepository(ABC):
    @abstractmethod
    def get_by_customer_id(self, customer_id):
        pass

    @abstractmethod
    def add(self, cart):
        pass

    @abstractmethod
    def update(self, cart):
        pass

    @abstractmethod
    def delete(self, cart_id):
        pass
