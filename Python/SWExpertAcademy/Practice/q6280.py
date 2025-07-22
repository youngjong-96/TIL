num = int(input())
yaksu = []
for i in range(1, num+1):
    if num % i==0:
        yaksu.append(i)
print(yaksu)