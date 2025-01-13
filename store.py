from typing import List, Tuple
from products import Product

class Store:
    """Represents a store containing products."""

    def __init__(self):
        """Initialize the store with an empty list of products."""
        self.products = []

    def add_product(self, product: Product):
        """Add a product to the store.

        Args:
            product (Product): The product to be added.
        """
        self.products.append(product)

    def remove_product(self, product: Product):
        """Remove a product from the store if it exists.

        Args:
            product (Product): The product to be removed.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Calculate the total quantity of all products in the store.

        Returns:
            int: Total quantity of products.
        """
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Get a list of all active products in the store.

        Returns:
            List[Product]: List of active products.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """Process an order and calculate the total price.

        Args:
            shopping_list (List[Tuple[Product, int]]): A list of tuples containing products and quantities to be purchased.

        Returns:
            float: Total price for the order.

        Raises:
            Exception: If a product is not in the store or cannot fulfill the order quantity.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise Exception(f"Product {product.name} is not in the store.")
            total_price += product.buy(quantity)
        return total_price
