#구구단 단을 입력받아 출력

def print_gugu(N):
    for i in range(1,10):
        print(f"{N} * {i} = {N*i}")

while True:
    N = int(input())
    if 1 < N <= 9:
        print_gugu(N)
        break
    else:
        print("1~9의 정수값을 입력하세요")