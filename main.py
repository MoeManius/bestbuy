from products import Product
from store import Store

def setup_store() -> Store:
    """Set up initial stock of inventory and return a store instance."""
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]
    store = Store()
    for product in product_list:
        store.add_product(product)
    return store

def display_menu():
    """Display the main menu options."""
    print("\nWelcome to the Store!")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")

def handle_list_products(store: Store):
    """Handle the option to list all products in the store."""
    print("\nAll active products in the store:")
    for product in store.get_all_products():
        print(product.show())

def handle_total_quantity(store: Store):
    """Handle the option to show the total quantity of items in the store."""
    print("\nTotal quantity of items in the store:", store.get_total_quantity())

def handle_order(store: Store):
    """Handle the option to make an order."""
    shopping_list = []
    while True:
        product_name = input("Enter the product name (or 'done' to finish): ")
        if product_name.lower() == 'done':
            break
        try:
            quantity = int(input(f"Enter the quantity for {product_name}: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue

        product = next((p for p in store.products if p.name == product_name), None)
        if product:
            shopping_list.append((product, quantity))
        else:
            print(f"Product {product_name} not found in the store.")

    try:
        total_price = store.order(shopping_list)
        print("Total price for the order:", total_price)
    except Exception as e:
        print("An error occurred while processing the order:", e)

def start():
    """Start the store application."""
    store = setup_store()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            handle_list_products(store)
        elif choice == '2':
            handle_total_quantity(store)
        elif choice == '3':
            handle_order(store)
        elif choice == '4':
            print("Thank you for visiting the store!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    start()
