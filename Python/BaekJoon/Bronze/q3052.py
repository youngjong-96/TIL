num_list = []
mod_list = []

for _ in range(10):
    num_list.append(int(input()))

for num in num_list:
    mod_list.append(num % 42)

print(len(set(mod_list)))