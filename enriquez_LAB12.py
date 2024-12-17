class FoodOrderingSystem:
    def __init__(self):
        self.menu = {
            "Burger": 5.99,
            "Pizza": 8.99,
            "Salad": 4.99,
            "Pasta": 7.99,
            "Soda": 1.99
        }
        self.order = {}

    def display_menu(self):
        print("\nMenu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price:.2f}")

    def take_order(self):
        while True:
            self.display_menu()
            choice = input("Enter the food item you'd like to order (or type 'done' to finish): ").strip()

            if choice.lower() == 'done':
                break

            if choice in self.menu:
                quantity = input(f"How many {choice}s would you like? ").strip()
                if quantity.isdigit():
                    quantity = int(quantity)
                    if choice in self.order:
                        self.order[choice] += quantity
                    else:
                        self.order[choice] = quantity
                    print(f"Added {quantity} {choice}(s) to your order.")
                else:
                    print("Please enter a valid quantity.")
            else:
                print("Sorry, we don't have that item. Please choose from the menu.")

    def display_order(self):
        print("\nYour Order:")
        total = 0
        for item, quantity in self.order.items():
            item_total = self.menu[item] * quantity
            total += item_total
            print(f"{item} (x{quantity}): ${item_total:.2f}")
        print(f"Total: ${total:.2f}")
        return total

    def process_payment(self, total):
        while True:
            try:
                cash = float(input(f"\nYour total is ${total:.2f}. Please enter your payment amount: $"))
                if cash >= total:
                    change = cash - total
                    print(f"Payment accepted. Your change is ${change:.2f}. Thank you for your order!")
                    break
                else:
                    print(f"Insufficient payment. You still owe ${total - cash:.2f}.")
            except ValueError:
                print("Invalid input. Please enter a valid payment amount.")

    def run(self):
        print("Welcome to the Food Ordering System!")
        self.take_order()
        if self.order:
            total = self.display_order()
            self.process_payment(total)
        else:
            print("You didn't order anything. Goodbye!")

if __name__ == "__main__":
    system = FoodOrderingSystem()
    system.run()
