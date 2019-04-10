import sys

from orders import load_orders, save_orders
from commands import list_orders, create_order, get_order

def cli():
    if len(sys.argv) == 1:
        print("Please specify a command!")
        print("Options: get, create, list, remove")
        exit(-1)

    command = sys.argv[1]
    path = './order.txt'
    orders = load_orders(path)

    if command == 'list':
        list_orders(orders)
    elif command == 'get':
        if len(sys.argv) == 2: 
            print("Please enter a value to search for!")
            exit(-1)
        
        order = get_order(orders, sys.argv[2])
        print(f'Item: {order["item"]} Quantity: {order["quantity"]}')
    elif command == 'remove':
        if len(sys.argv) == 2: 
            print("Please enter a value to search for!")
            exit(-1)
        
        order = get_order(orders, sys.argv[2])
        orders.remove(order)
        save_orders(path, orders)
        
        print("1 order removed!")
    elif command == 'create':
        if len(sys.argv) == 4:
            item_name = sys.argv[2]
            quantity = int(sys.argv[3])

            create_order(orders, item_name, quantity)
            save_orders(path, orders)
        else:
            print("Please enter a value to search for!")
            exit(-1)
    else:
        print("Please enter a valid command!")
        print("Options: get, create, list, remove")
        exit(-1)

if __name__ == '__main__':
    cli()