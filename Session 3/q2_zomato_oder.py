zomato_order_price = input("Enter an order price :")

order_price = float(zomato_order_price)

gst_amount = order_price * 0.18

final_bill = order_price + gst_amount

print(f'Final Bill : {final_bill} with GST 18%')