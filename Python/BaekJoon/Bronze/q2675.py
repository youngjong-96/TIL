# 문자열 반복

T = int(input())

for i in range(T):
    # R = 반복 횟수, S = 문자열
    R, S = input().split()

    ns = ""

    for i in S:
        ns = ns + (i * int(R))

    print(f"{ns}")
