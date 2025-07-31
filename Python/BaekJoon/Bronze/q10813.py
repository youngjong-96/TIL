# 공 바꾸기 (브론즈2)

# 바구니를 총 N개, M번 공을 바꾼다
N, M = map(int, input().split())

baguny = []
for num in range(1, N+1):
    baguny.append(num)

for num in range(1, M+1):
    i, j = map(int, input().split())
    baguny[i-1], baguny[j-1] = baguny[j-1], baguny[i-1]

print(" ".join(map(str, baguny)))    
    