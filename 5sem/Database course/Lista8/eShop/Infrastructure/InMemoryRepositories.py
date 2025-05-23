from typing import List, TypeVar, Generic
from uuid import UUID
from ..Domain.Entities import Cart, Order, Product
from ..Domain import ProductRepository, CartRepository, OrderRepository

T = TypeVar("T")


class InMemoryRepository(Generic[T]):
    def __init__(self):
        self.items = []

    def get(self, item_id: UUID) -> T:
        return next((item for item in self.items if item.id == item_id), None)

    def add(self, item):
        self.items.append(item)

    def update(self):
        pass

    def delete(self, item_id: UUID):
        filtered = list(filter(lambda item: item.id != item_id, self.items))
        self.items = filtered


class InMemoryProductRepository(InMemoryRepository[Product], ProductRepository):
    pass


class InMemoryCartRepository(InMemoryRepository[Cart], CartRepository):
    pass


class InMemoryOrderRepository(InMemoryRepository[Order], OrderRepository):
    pass
