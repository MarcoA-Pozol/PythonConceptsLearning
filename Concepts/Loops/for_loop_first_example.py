"""
    for i in range() loop.

    We are going to simulate a system that iterates over every item price on the list of items, checking if this item is in discount, or not.    
"""

# List of tuples(items data) / (item_name, price, units, have_discount, dicount_amount)
items = [('Cheese 345gr', 12.59, 1, False, 1.50), ('Milk 1L', 6.99, 2, True, .49), ('Eggs Dozen', 8.19, 2, False, 2.00), ('Orange Juice 500ml', 3.50, 3, True, 0.20), ('Bread 500gr', 4.59, 2, False, 0.30)]
ticket = {'total_to_pay':0, 'items_with_discount':0, 'total_discount':0}

# Iterating the list of items
for item in items:
    ticket['total_to_pay'] = ticket['total_to_pay'] + (item[2] * item[1]) # Applying total price based on the amount of units.
    if item[3]:
        ticket['total_discount'] = ticket['total_discount'] + (item[4] * item[2])
        ticket['items_with_discount'] += 1
    
total_without_discount = ticket['total_to_pay']
ticket['total_to_pay'] = ticket['total_to_pay'] - ticket['total_discount']

print(f'Without Discount: {round(total_without_discount, 2)}\nDiscounted: {round(ticket['total_discount'], 2)}\nTotal: {round(ticket['total_to_pay'], 2)}')