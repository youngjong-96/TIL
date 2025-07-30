# 최댓값 구하기
num_list = {}

for i in range(9):
    num_list[int(input())] = i+1

max_value = list(num_list.keys())[0]

for num in num_list:
    if num > max_value:
        max_value = num

print(max_value)
print(num_list[max_value])