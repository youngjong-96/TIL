T = int(input())
result_lst = []

for _ in range(T):
    # N = 갯수, ai = 리스트
    N = int(input())
    ai = list(map(int, input().split()))

    # 초기값 설정
    max_v = ai[0]
    min_v = ai[0]

    # 순회하며 최댓값과 최솟값 저장
    for i in range(N):
        if max_v < ai[i]:
            max_v = ai[i]
        if min_v > ai[i]:
            min_v = ai[i]

    result = max_v - min_v
    result_lst.append(result)

for i in range(len(result_lst)):
    print(f"#{i + 1} {result_lst[i]}")