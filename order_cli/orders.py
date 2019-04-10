ITEM_NAME_COLUMN = 0
QUANTITY_COLUMN = 1

# This function, reads a text file and returns a list of dictionaries
def load_orders(path):
    orders = []
    
    # Open the file as read only
    with open(path, 'r') as order_file:
        # Read each line
        for line in order_file.readlines():
            # Split by commas
            order = line.rstrip().split(',')

            # Get our data from the columns
            item_name = order[ITEM_NAME_COLUMN]
            quantity = int(order[QUANTITY_COLUMN])

            # Create a human readable dictionary
            item = {
                'item': item_name,
                'quantity': quantity,
            }
            orders.append(item)

    return orders


# This function takes a list of dictionaries and saves data into the file
def save_orders(path, orders):
    # Open the file at path with write mode
    with open(path, 'w') as order_file:
        # Iterate over our list of dictionaries
        for order in orders:
            # Create a text line
            line = f'{order["item"]},{order["quantity"]}\n'
            # And write it to the file!
            order_file.write(line)
