#main code#
from operation import order_from_manufacturer, sell_to_customer
from read import read_inventory

def display_inventory(inventory):
    print("\nCurrent Inventory:")
    print(f"{'ID':<5} {'Manufacturer':<25} {'Product':<20} {'Quantity':<10} {'Price':<10}")
    print("-" * 75)
    for id, details in inventory.items():
        print(f"{id:<5} {details['manufacturer']:<25} {details['product_name']:<20} {details['quantity']:<10} ${details['price']:<10.2f}")
    print("\n")

def main():
    while True:
        print("Welcome to BRJ Furniture Store Management System")
        print("Please select an option:")
        print("1. Display all available furniture")
        print("2. Order furniture from manufacturer")
        print("3. Sell furniture to customer")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            inventory = read_inventory()
            display_inventory(inventory)
        elif choice == '2':
            employee_name = input("Enter the name of the employee ordering the furniture: ")
            details = f"Employee: {employee_name}"
            items = []
            
            while True:
                try:
                    id = int(input("Enter the ID of the furniture to order: "))
                    quantity = int(input("Enter the quantity to order: "))
                    items.append({'id': id, 'quantity': quantity})
                except ValueError:
                    print("Invalid input. Please enter numeric values for ID and quantity.")
                    continue
                
                more = input("Do you want to order more items? (yes/no): ")
                if more.lower() != 'yes':
                    break
                
            
            order_invoice = order_from_manufacturer(details, items)
            print(f"Order invoice generated: {order_invoice}")
        elif choice == '3':
            customer_name = input("Enter the name of the customer: ")
            details = f"Customer: {customer_name}"
            items = []
            
            while True:
                try:
                    id = int(input("Enter the ID of the furniture to sell: "))
                    quantity = int(input("Enter the quantity to sell: "))
                    items.append({'id': id, 'quantity': quantity})
                except ValueError:
                    print("Invalid input. Please enter numeric values for ID and quantity.")
                    continue
                
                more = input("Do you want to sell more items? (yes/no): ")
                if more.lower() != 'yes':
                    break
            
            sale_invoice = sell_to_customer(details, items)
            print(f"Sale invoice generated: {sale_invoice}")
        elif choice == '4':
            print("Thank you for using BRJ Furniture Store Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        # Ask if the user wants to choose more options
        more_options = input("Do you want to choose from BRJ management store (yes/no): ")
        if more_options.lower() != 'yes':
            print("Thank you for using BRJ Furniture Store Management System. Goodbye!")
            break

if __name__ == "__main__":
    main()
