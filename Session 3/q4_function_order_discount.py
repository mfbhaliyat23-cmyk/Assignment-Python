def is_discount_applicable(order_amount):
    if order_amount > 500:
        return True
    else:
        return False

order_1 = 450.0
order_2 = 550.0

print(f"Is discount applicable for ₹{order_1}? {is_discount_applicable(order_1)}")
print(f"Is discount applicable for ₹{order_2}? {is_discount_applicable(order_2)}")
