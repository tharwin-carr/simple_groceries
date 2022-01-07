'''
Store service is used to calculate the total cost of the
grocery list and see if user has enough  money.
'''

def purchase_items(user_money_arg, items):
    items_total_cost = 0
    for item in items:
        items_total_cost = items_total_cost + item
    if items_total_cost <= user_money_arg:
        amount_left = user_money_arg - items_total_cost
        print(f'Purchase Complete: ${amount_left} left')
    else:
        print('You cannot afford all of these items.')