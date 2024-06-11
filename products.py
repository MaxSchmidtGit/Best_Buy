from typing import Optional
from promotions import Promotion


class Product:
    """Represents a product in the store."""

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a new product.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in stock.

        Raises:
            ValueError: If name is empty or price/quantity is negative.
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid value for name, price or quantity")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion: Optional[Promotion] = None

    def get_quantity(self) -> int:
        """Returns the quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Sets the quantity of the product.

        Args:
            quantity (int): The new quantity of the product.

        Raises:
            ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def set_promotion(self, promotion: Promotion):
        """Sets a promotion for the product."""
        self.promotion = promotion

    def get_promotion(self) -> Optional[Promotion]:
        """Returns the current promotion for the product."""
        return self.promotion

    def show(self) -> str:
        """Returns a string representation of the product."""
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promotion_info}"

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product.

        Args:
            quantity (int): The quantity to buy.

        Raises:
            ValueError: If quantity is less than or equal to zero or more than available stock.

        Returns:
            float: The total price of the purchase.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity in stock")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity


class NonStockedProduct(Product):
    """Represents a non-stocked product in the store."""

    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)
        self.active = True  # NonStockedProducts are always active

    def set_quantity(self, quantity: int):
        pass  # Quantity is always zero for non-stocked products

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity

    def show(self) -> str:
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return (
            f"{self.name}, Price: {self.price}, Quantity: Not applicable (Non-stocked product)"
            f"{promotion_info}"
        )


class LimitedProduct(Product):
    """Represents a limited product in the store."""

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} of this product in one order")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity in stock")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity

    def show(self) -> str:
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return (
            f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Max per order: {self.maximum}"
            f"{promotion_info}"
        )
