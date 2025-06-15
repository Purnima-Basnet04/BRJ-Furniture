import datetime
from read import read_inventory
from write import write_inventory

def generate_invoice(transaction_type, details, items, inventory, shipping_cost):
    try:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        filename = f"{transaction_type}_invoice_{timestamp}.txt"
        
        with open(filename, 'w') as file:
            file.write(f"{transaction_type.capitalize()} Invoice\n")
            file.write(f"Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(f"Details: {details}\n\n")
            
            total_amount = 0
            file.write("Items:\n")
            for item in items:
                id = item['id']
                quantity = item['quantity']
                
                if id not in inventory:
                    raise ValueError(f"Error: Furniture ID {id} does not exist in the inventory.")
                
                inventory_item = inventory[id]
                price = inventory_item['price']
                amount = quantity * price
                total_amount += amount
                
            
                file.write(f"ID: {id}, Manufacturer: {inventory_item['manufacturer']}, "
                           f"Product: {inventory_item['product_name']}, Quantity: {quantity}, "
                           f"Price: ${price:.2f}, Amount: ${amount:.2f}\n")
            
            vat = total_amount * 0.13
            total_amount_with_vat = total_amount + vat
            total_amount_with_shipping = total_amount_with_vat + shipping_cost
            
            file.write("============================================================")
            file.write(f"\nTotal Amount: ${total_amount:.2f}\n")
            file.write(f"VAT (13%): ${vat:.2f}\n")
            file.write(f"Total Amount with VAT: ${total_amount_with_vat:.2f}\n")
            
            file.write(f"Shipping Cost: ${shipping_cost:.2f}\n")
            file.write(f"Total Amount to be Paid: ${total_amount_with_shipping:.2f}\n")
        
        return filename
    
    except Exception as e:
        print(f"An error occurred while generating the invoice: {e}")
        return None

def get_shipping_cost():
    while True:
        try:
            shipping_cost = float(input("Enter the shipping cost: $"))
            if shipping_cost <= 0:
                raise ValueError("Shipping cost must be greater than 0.")
            return shipping_cost
        except ValueError as e:
            print(e)

def order_from_manufacturer(details, items):
    try:
        inventory = read_inventory()
        shipping_cost = get_shipping_cost()  # Get the validated shipping cost from the user
        for item in items:
            id = item['id']
            quantity = item['quantity']
            if id in inventory:
                inventory[id]['quantity'] += quantity
            else:
                print(f"Error: Furniture ID {id} does not exist.")
        
        write_inventory(inventory)
        return generate_invoice('order', details, items, inventory, shipping_cost)
    
    except Exception as e:
        print(f"An error occurred during the order process: {e}")
        return None

def sell_to_customer(details, items):
    try:
        inventory = read_inventory()
        shipping_cost = get_shipping_cost()  # Get the validated shipping cost from the user
        for item in items:
            id = item['id']
            quantity = item['quantity']
            if id in inventory:
                if inventory[id]['quantity'] >= quantity:
                    inventory[id]['quantity'] -= quantity
                else:
                    print(f"Error: Not enough stock for Furniture ID {id}.")
            else:
                print(f"Error: Furniture ID {id} does not exist.")
        
        write_inventory(inventory)
        return generate_invoice('sale', details, items, inventory, shipping_cost)
    
    except Exception as e:
        print(f"An error occurred during the sales process: {e}")
        return None
