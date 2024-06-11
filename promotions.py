from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        pass


class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        return product.price * quantity * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity: int) -> float:
        full_price_count = quantity // 2 + quantity % 2
        half_price_count = quantity // 2
        return (
            full_price_count * product.price +
            half_price_count * product.price * 0.5
        )


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity: int) -> float:
        full_price_count = quantity - (quantity // 3)
        return full_price_count * product.price
