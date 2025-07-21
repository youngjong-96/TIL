#백만장자 프로젝트
T = int(input())

for j in range(T):
    N = int(input())
    price_list = list(map(int, input().split()))
    
    Max_price_list = [0]*N
    Max_price = price_list[N-1]
    
    for i in range(N-1,-1,-1):
        if price_list[i] > Max_price:
            Max_price_list[N-i-1] = price_list[i]
            Max_price = price_list[i]
        else:
            Max_price_list[N-i-1] = Max_price
    
    benefit = 0
    
    for i in range(N):
        # if Max_price_list[i] - price_list[i] > 0:
            benefit += (Max_price_list[i] - price_list[i])
    
    print(f"#{j+1} {benefit}")