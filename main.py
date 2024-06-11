import products
import store

# Setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = store.Store(product_list)


def start(store):
    while True:
        print("\n1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Please choose a number: ")

        if choice == '1':
            list_products(store)
        elif choice == '2':
            show_total_amount(store)
        elif choice == '3':
            make_order(store)
        elif choice == '4':
            print("Thank you for using the store management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def list_products(store):
    products = store.get_all_products()
    print("\nProducts in store:")
    for product in products:
        print(product.show())


def show_total_amount(store):
    total_quantity = store.get_total_quantity()
    print(f"\nTotal amount in store: {total_quantity}")


def make_order(store):
    products = store.get_all_products()
    print("\nProducts available for order:")
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product.show()}")

    order = []
    while True:
        product_number = input("Enter the product number to order (or 'done' to finish): ")
        if product_number.lower() == 'done':
            break
        if not product_number.isdigit() or int(product_number) < 1 or int(product_number) > len(products):
            print("Invalid product number. Please try again.")
            continue

        product_quantity = input("Enter the quantity: ")
        if not product_quantity.isdigit() or int(product_quantity) <= 0:
            print("Invalid quantity. Please try again.")
            continue

        product = products[int(product_number) - 1]
        order.append((product, int(product_quantity)))

    if order:
        try:
            total_cost = store.order(order)
            print(f"Order placed successfully. Total cost: ${total_cost}")
        except Exception as e:
            print(f"Error placing order: {e}")


if __name__ == "__main__":
    start(best_buy)