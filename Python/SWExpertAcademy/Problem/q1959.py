# 두 개의 숫자열
# 서로 다른 3이상 20이하의 길이에 임의의 숫자를 가지는 숫자열을 서로 마주보는 숫자를 곱할 때, 최댓값을 구하기

T = int(input())

result_list = []

for test in range(1,T+1):
    S, L = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if S > L:
        L, S = S, L
        A, B = B, A

    result = 0.0

    for i in range(L-S+1):
        sum = 0
        for j in range(S):
            sum += A[j] * B[j+i]
        if sum > result:
            result = sum
            
    # result_list.append(result)
    print(f"#{test} {result}")

# for i in range(T):
#     print(f"#{T+1} {result_list[T]}")