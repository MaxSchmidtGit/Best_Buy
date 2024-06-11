import products
import promotions
import store as store_module  # Verwenden Sie einen Alias, um Konflikte zu vermeiden


def start(store_instance):
    while True:
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Please choose a number: ")

        if choice == '1':
            list_products(store_instance)
        elif choice == '2':
            show_total_amount(store_instance)
        elif choice == '3':
            make_order(store_instance)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


def list_products(store_instance):
    products_list = store_instance.get_all_products()
    for product in products_list:
        print(product.show())


def show_total_amount(store_instance):
    print(f"Total amount in store: {store_instance.get_total_quantity()} items")


def make_order(store_instance):
    products_list = store_instance.get_all_products()
    shopping_list = []
    while True:
        for i, product in enumerate(products_list):
            print(f"{i + 1}. {product.show()}")
        product_number = input("Enter the product number to order (or 'done' to finish): ")
        if product_number.lower() == 'done':
            break
        quantity = int(input("Enter the quantity: "))
        product = products_list[int(product_number) - 1]
        shopping_list.append((product, quantity))
    total_price = store_instance.order(shopping_list)
    print(f"Order cost: {total_price} dollars.")


# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
    products.NonStockedProduct("Windows License", price=125),
    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]

best_buy = store_module.Store(product_list)

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

if __name__ == "__main__":
    start(best_buy)
