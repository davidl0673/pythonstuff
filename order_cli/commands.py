def list_orders(orders):
    print(f"There are currently {len(orders)} orders!\n")
    for order in orders:
        print(f'Item: {order["item"]} Quantity: {order["quantity"]}')

def get_order(orders, item_name):
    for order in orders:
        if order['item'].casefold() == item_name.casefold():
            return order


def create_order(orders, item_name, quantity):
    orders.append({
        'item': item_name,
        'quantity': quantity
    })