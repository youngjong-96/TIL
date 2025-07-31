#각 물건의 가격과 개수 출력, 총 금액과 비교

total_price = int(input())

N = int(input())

result = 0

for i in range(N):
    a, b = map(int, input().split())
    result += a*b
    
if total_price == result:
    print("Yes")
else:
    print("No")