n = int(input())

for i in range(n):
    print(" " * (4-i), end="")
    print("*" * (1 + (i * 2)))

for i in range(n-1):
    print(" " * (i + 1), end="")
    print("*" * (7-(i*2)))