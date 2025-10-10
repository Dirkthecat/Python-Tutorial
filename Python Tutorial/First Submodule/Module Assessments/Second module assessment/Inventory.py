class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}")

    def update_quantity(self, amount):
        if self.quantity + amount < 0:
            print(f"Error: Not enough {self.name} in stock.")
        else:
            self.quantity += amount
            print(f"Updated quantity for {self.name}: {self.quantity}")

    def total_value(self):
        return self.price * self.quantity

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, name, price, quantity):
        if name in self.products:
            self.products[name].update_quantity(quantity)
        else:
            self.products[name] = Product(name, price, quantity)
            print(f"Product {name} added successfully.")

    def display_inventory(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            print("\n--- Inventory ---")
            for product in self.products.values():
                product.display_info()

    def update_product_quantity(self, name, amount):
        if name in self.products:
            self.products[name].update_quantity(amount)
        else:
            print(f"No product found with name '{name}'.")

    def calculate_total_inventory_value(self):
        total = sum(p.total_value() for p in self.products.values())
        print(f"Total inventory value: ${total:.2f}")


def main():
    print("Inventory system starting...\n")
    store_inventory = Inventory()

    store_inventory.add_product("Sample Product", 10.0, 5)

    while True:
        print("\n--- Inventory Menu ---")
        print("1. Add Product")
        print("2. Display Inventory")
        print("3. Update Product Quantity")
        print("4. Calculate Total Inventory Value")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            store_inventory.add_product(name, price, quantity)
        elif choice == '2':
            store_inventory.display_inventory()
        elif choice == '3':
            name = input("Enter product name to update: ")
            amount = int(input("Enter quantity change (negative for sold): "))
            store_inventory.update_product_quantity(name, amount)
        elif choice == '4':
            store_inventory.calculate_total_inventory_value()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
