def remove_last_item(order_list):
    removed_item = order_list.pop()
    return removed_item

zomato_order_list = ['Paneer','Dosa','Butter Naan','Juice']
print(f'The original list : {zomato_order_list}')
result = remove_last_item(zomato_order_list)

print(f'Final_list : {zomato_order_list}')
print(f'Removed item : {result}')