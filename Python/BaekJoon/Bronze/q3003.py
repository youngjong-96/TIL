count = list(map(int, input().split()))

std = [1, 1, 2, 2, 2, 8]

result = []

for i in range(len(count)):
    result.append(std[i] - count[i])


print(" ".join(map(str, result)))