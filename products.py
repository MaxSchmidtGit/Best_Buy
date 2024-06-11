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

    def show(self) -> str:
        """Returns a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

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
        return self.price * quantity


# Example usage
if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())
