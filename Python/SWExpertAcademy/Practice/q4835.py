T = int(input())
result_list = []

for _ in range(T):
    N, M = map(int, input().split()) # N = 정수의 개수, M = 구간의 크기
    ai = list(map(int, input().split()))

    lst = [] # M 크기 구간 별 모든 합을 저장할 리스트

    for i in range(N-M+1): # (정수의 개수 - 구간의 크기 +1) 개의 합
        sum = 0
        for j in range(M): # M 크기 구간만큼 한 칸씩 옆으로 가면서 더하기
            sum += ai[i+j]
        lst.append(sum)

    # 최댓값, 최솟값 구하기
    max_v = lst[0]
    min_v = lst[0]

    for i in range(len(lst)):
        if max_v < lst[i]:
            max_v = lst[i]
        if min_v > lst[i]:
            min_v = lst[i]

    # 결과를 결과 리스트에 추가
    result = max_v - min_v
    result_list.append(result)

# 결과 출력
for i in range(T):
    print(f"#{i+1} {result_list[i]}")
