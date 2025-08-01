n = int(input())

for i in range(0, n-1):
    print(" " * (n-(i+1)), end="")
    print("*" * (1 + (i * 2)))

print("*" * ((n*2)-1))

for i in range(n-2, -1, -1):
    print(" " * (n - i - 1), end="")
    print("*" * (1 + (i * 2)))