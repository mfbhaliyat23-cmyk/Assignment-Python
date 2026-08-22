product_names =[' mi-Band 5 ', ' SAMSUNG-Galaxy ', ' realme-Book ']

cleaned_list = []

for name in product_names:
    cleaned_name = name.strip().replace(' ','-').title()

    cleaned_list.append(cleaned_name)

print(cleaned_list)