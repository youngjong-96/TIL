# 가격에 따라 내림차순

product = {"TV": 2000000,
"냉장고": 1500000,
"책상": 350000,
"노트북": 1200000,
"가스레인지": 200000,
"세탁기": 1000000}

# print(product.items())
def get_value(tuple):
    return tuple[1]

sorted_product = sorted(product.items(), key=get_value, reverse=True)

for key, value in sorted_product:
    print(f'{key}: {value}')