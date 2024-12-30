from products import Product

def main():
    try:
        # Test creation of a product
        product1 = Product("MacBook Air M2", 999.99, 10)
        print(product1.show())

        # Test getting quantity
        print("Quantity:", product1.get_quantity())

        # Test setting quantity
        product1.set_quantity(5)
        print("Updated Quantity:", product1.get_quantity())

        # Test buying product
        total_price = product1.buy(2)
        print("Total price for 2 units:", total_price)
        print(product1.show())

        # Test buying more than available quantity
        try:
            product1.buy(10)
        except Exception as e:
            print("Exception:", e)

        # Test deactivating and reactivating product
        product1.deactivate()
        print("Is product active?", product1.is_active())
        product1.activate()
        print("Is product active?", product1.is_active())

        # Test invalid product creation
        try:
            invalid_product = Product("", -100, -5)
        except ValueError as e:
            print("Exception:", e)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
