# 전기버스

# 버스는 0에서 출발해 N 까지 간다
# K : 한 번 충전으로 이동할 수 있는 최대 정류장 수
# M : 충전기가 설치된 정류장 개수
# M_lst : 충전기 설치 정류장 리스트

T = int(input())

for t in range(T):
    K, N, M = map(int,input().split())
    M_list = [0] + list(map(int, input().split()))
    M_list.append(N)
    
    # 충전소 방문 횟수
    result = 0
    
    # 충전 안하고 지나칠 경우의 소모값
    used = 0
    
    for i in range(len(M_list)-1):
        while i < len(M_list)-2:    
            if M_list[i] + K < M_list[i + 1]:
                result = 0
                break
            elif M_list[i] + K - used <= M_list[i + 2]:
                result += 1
                used = 0
            elif M_list[i] + K - used > M_list[i + 2]:
                used += M_list[i + 1] - M_list[i]
    
    print(f"#{t+1} {result}")
    