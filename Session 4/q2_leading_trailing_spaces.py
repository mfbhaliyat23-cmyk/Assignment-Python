def clean_brand_name(name):
    return name.strip().replace("-"," ")

test_input = '  Oneplus-Nord  '
result = clean_brand_name(test_input)

print('Input  :',test_input)
print('Output :',result)