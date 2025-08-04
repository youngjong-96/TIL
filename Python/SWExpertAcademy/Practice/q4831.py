# 전기버스

# 버스는 0에서 출발해 N 까지 간다
# K : 한 번 충전으로 이동할 수 있는 최대 정류장 수
# M : 충전기가 설치된 정류장 개수
# M_lst : 충전기 설치 정류장 리스트

T = int(input())

for t in range(T):
    K, N, M = map(int,input().split())
    bus_stop = [0] + list(map(int, input().split()))
    bus_stop.append(N)
    
    # 충전소 방문 횟수
    result = 0
    
    # 충전 안하고 지나칠 경우의 소모값
    used = 0
    
    for i in range(len(bus_stop)-2):
        # 다음 충전소까지 거리    
        l = bus_stop[i + 1] - bus_stop[i]
        # 다다음 충전소까지 거리
        l2 = bus_stop[i + 2] - bus_stop[i]
        
        
        if K < l:  # 다음 충전소까지 못가면 0
            result = 0
            break
        elif l <= K - used < l2: # 다음 충전소까지는 되지만 그 다음은 안되면 들린다
            result += 1
            used = 0
        elif K - used >= l2: # 한 번에 다다음까지 갈 수 있으면 지나쳐가고 그 거리만큼 소모값 증가
            used += l
            
    # 마지막 정류소로부터 도착지 비교
    if K - used < bus_stop[-1] - bus_stop[-2]:
        result = 0
    
    print(f"#{t+1} {result}")
    