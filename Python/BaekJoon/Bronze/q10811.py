# N 개의 바구니, M번 바꿈

baguny = []

N, M = map(int, input().split())

for i in range(1, N+1):
    baguny.append(i)

for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        baguny[i-1:j] = baguny[j-1::-1]
    else:
        baguny[i-1:j] = baguny[j-1:i-2:-1]
    
    #쉬운 방법
    # baguny[i-1:j] = reversed(baguny[i-1:j])

print(" ".join(map(str, baguny)))



# a = [1, 2, 3, 4, 5]
# # 3번째부터 5번째
# # a[2:4] = a[4:1:-1]
# print(a[2:5])
# print(a[4:1:-1])
# print(a)
