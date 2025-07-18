list = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]

def odd_num(list):
    odd_list = [i for i in list if i%2==0]
    return odd_list

print(odd_num(list))