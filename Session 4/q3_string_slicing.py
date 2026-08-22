brand_name = 'Apple iPhone 14 Pro Max'

brand_length = len(brand_name.split()[0])

brand = brand_name[:brand_length]
model = brand_name[brand_length + 1:]

print(brand)
print(model)