S = input()

result = []

for i in range(97,123):
    result.append(S.find(chr(i)))

print(" ".join(map(str, result)))