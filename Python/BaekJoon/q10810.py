# 공 넣기

# M = 바구니 수이자 끝번호
# N = 공을 넣을 횟수
M, N = map(int, input().split())

basket = [0] * M

# i번 바구니부터 j번 바구니까지 k번 번호가 적힌 공을 넣는다
for _ in range(N):
    i, j, k = map(int, input().split())
    basket[i-1:j] = [k] * (j - i + 1)

print(" ".join(map(str,basket)))


