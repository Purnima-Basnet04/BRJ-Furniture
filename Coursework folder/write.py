def write_inventory(inventory, filename='furniture.txt'):
    with open(filename, 'w') as file:
        for id, details in inventory.items():
            line = f"{id}, {details['manufacturer']}, {details['product_name']}, {details['quantity']}, ${details['price']:.2f}\n"
            file.write(line)
