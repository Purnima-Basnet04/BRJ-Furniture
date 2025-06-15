def read_inventory(filename='furniture.txt'):
    inventory = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(', ')
            id = int(parts[0])
            manufacturer = parts[1]
            product_name = parts[2]
            quantity = int(parts[3])
            price = float(parts[4].strip("$"))
            
            inventory[id] = {
                'manufacturer': manufacturer,
                'product_name': product_name,
                'quantity': quantity,
                'price': price
            }
    return inventory
