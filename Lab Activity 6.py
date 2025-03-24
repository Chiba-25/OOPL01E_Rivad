from abc import ABC, abstractmethod

# Abstract Product class
class Product(ABC):
    def __init__(self, name, price):
        self._name = name  # Encapsulation
        self._price = price

    @abstractmethod
    def get_info(self):
        pass

# Electronics subclass
class Electronics(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price)
        self._warranty_period = warranty_period

    def get_info(self):
        return f"{self._name} (₱{self._price}) - Warranty: {self._warranty_period} years"

# Clothing subclass
class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self._size = size

    def get_info(self):
        return f"{self._name} (₱{self._price}) - Size: {self._size}"

# ShoppingCart class
class ShoppingCart:
    def __init__(self):
        self._cart = []

    def add_to_cart(self, product, quantity):
        self._cart.append({'product': product, 'quantity': quantity})
        print(f"Added {quantity} x {product._name} to cart.")

    def view_cart(self):
        if not self._cart:
            print("\nShopping Cart is empty.")
        else:
            print("\nShopping Cart:")
            total_price = 0
            for i, item in enumerate(self._cart, 1):
                product = item['product']
                quantity = item['quantity']
                subtotal = product._price * quantity
                total_price += subtotal
                print(f"{i}. {product.get_info()} - Quantity: {quantity} - Subtotal: ₱{subtotal}")
            print(f"Total Price: ₱{total_price}")

    def checkout(self):
        if not self._cart:
            print("\nCart is empty. Nothing to checkout.")
        else:
            total_price = sum(item['product']._price * item['quantity'] for item in self._cart)
            print(f"\nTotal Price: ₱{total_price}")
            self._cart.clear()
            print("Checkout complete! Cart is now empty.")

# Main program with user interaction
if __name__ == "__main__":
    cart = ShoppingCart()

    while True:
        print("\nShopping Cart Menu:")
        print("1. Add Electronics")
        print("2. Add Clothing")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter the name of the electronic item: ")
            price = float(input("Enter the price: ₱"))
            warranty = int(input("Enter the warranty period (in years): "))
            quantity = int(input("Enter the quantity: "))
            product = Electronics(name, price, warranty)
            cart.add_to_cart(product, quantity)

        elif choice == '2':
            name = input("Enter the name of the clothing item: ")
            price = float(input("Enter the price: ₱"))
            size = input("Enter the size (e.g., Small, Medium, Large): ")
            quantity = int(input("Enter the quantity: "))
            product = Clothing(name, price, size)
            cart.add_to_cart(product, quantity)

        elif choice == '3':
            cart.view_cart()

        elif choice == '4':
            cart.checkout()

        elif choice == '5':
            print("Exiting the Shopping Cart System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
