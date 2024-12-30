from products import Product
from store import Store

def main():
    try:
        # Create some products
        product1 = Product("MacBook Air M2", 999.99, 10)
        product2 = Product("iPhone 13", 799.99, 5)
        product3 = Product("Apple Watch", 399.99, 20)

        # Create a store and add products to it
        store = Store()
        store.add_product(product1)
        store.add_product(product2)
        store.add_product(product3)

        # Display all active products in the store
        print("All active products in the store:")
        for product in store.get_all_products():
            print(product.show())

        # Get the total quantity of items in the store
        print("Total quantity of items in the store:", store.get_total_quantity())

        # Create a shopping list and place an order
        shopping_list = [(product1, 2), (product3, 5)]
        total_price = store.order(shopping_list)
        print("Total price for the order:", total_price)

        # Display all active products in the store after the order
        print("All active products in the store after the order:")
        for product in store.get_all_products():
            print(product.show())

        # Test removing a product
        store.remove_product(product2)
        print("After removing iPhone 13, all active products in the store:")
        for product in store.get_all_products():
            print(product.show())

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
