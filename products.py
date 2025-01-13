class Product:
    """Represents a product with a name, price, and quantity."""

    def __init__(self, name: str, price: float, quantity: int):
        """Initialize a new product.

        Args:
            name (str): The name of the product.
            price (float): The price of the product. Must be non-negative.
            quantity (int): The initial quantity of the product. Must be non-negative.

        Raises:
            ValueError: If name is empty, price is negative, or quantity is negative.
        """
        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Get the current quantity of the product.

        Returns:
            int: The quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """Set the quantity of the product and deactivate it if the quantity is zero.

        Args:
            quantity (int): The new quantity. Must be non-negative.

        Raises:
            ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Check if the product is active.

        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self) -> str:
        """Return a string representation of the product.

        Returns:
            str: A string containing the product's details.
        """
        return (
            f"Product: {self.name}, Price: ${self.price:.2f}, "
            f"Quantity: {self.quantity}, Active: {self.active}"
        )

    def buy(self, quantity: int) -> float:
        """Buy a specified quantity of the product.

        Args:
            quantity (int): The quantity to buy. Must be positive.

        Returns:
            float: The total price for the purchased quantity.

        Raises:
            ValueError: If the purchase quantity is not positive.
            Exception: If the product is inactive or there is insufficient quantity.
        """
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive.")
        if not self.active:
            raise Exception("Product is not active.")
        if quantity > self.quantity:
            raise Exception("Not enough quantity in stock.")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price
