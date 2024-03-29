class Medicine:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class MedicalStore:
    def __init__(self):
        self.inventory = {}

    def add_medicine(self, medicine):
        if medicine.name in self.inventory:
            self.inventory[medicine.name].quantity += medicine.quantity
        else:
            self.inventory[medicine.name] = medicine

    def sell_medicine(self, medicine_name, quantity):
        if medicine_name in self.inventory:
            if self.inventory[medicine_name].quantity >= quantity:
                self.inventory[medicine_name].quantity -= quantity
                total_price = quantity * self.inventory[medicine_name].price
                return f"Sold {quantity} units of {medicine_name}. Total Price: ${total_price}"
            else:
                return f"Insufficient stock for {medicine_name}. Available: {self.inventory[medicine_name].quantity}"
        else:
            return f"{medicine_name} not found in inventory."

    def delete_medicine(self, medicine_name):
        if medicine_name in self.inventory:
            del self.inventory[medicine_name]
            return f"{medicine_name} deleted from inventory."
        else:
            return f"{medicine_name} not found in inventory."

    def display_inventory(self):
        print("Inventory:")
        for medicine in self.inventory.values():
            print(f"{medicine.name} - Quantity: {medicine.quantity} - Price: ${medicine.price}")

# Example Usage:
if __name__ == "__main__":
    store = MedicalStore()

    while True:
        print("\nOptions:")
        print("1. Add new drug to inventory")
        print("2. Sell drug")
        print("3. Delete drug from inventory")
        print("4. Display inventory")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter drug name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per unit: "))
            new_medicine = Medicine(name, quantity, price)
            store.add_medicine(new_medicine)
            print(f"{name} added to inventory.")

        elif choice == "2":
            name = input("Enter drug name to sell: ")
            quantity = int(input("Enter quantity to sell: "))
            result = store.sell_medicine(name, quantity)
            print(result)

        elif choice == "3":
            name = input("Enter drug name to delete: ")
            result = store.delete_medicine(name)
            print(result)

        elif choice == "4":
            store.display_inventory()

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
