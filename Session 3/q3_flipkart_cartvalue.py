Flipkart_prices = ['199.99', '299.50', '150']

Float_prices = [float(price) for price in Flipkart_prices]

Total_cart_value = sum(Float_prices)
print(Total_cart_value)