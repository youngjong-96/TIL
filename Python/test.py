# 유기농 배추

import sys

sys.stdin = open('input.txt', 'r')
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
T = int(sys.stdin.readline().strip())
for t in range(1, T+1):
    # 배추밭의 가로길이 n(1 ≤ M ≤ 50)과 세로길이 m(1 ≤ N ≤ 50),그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 
    n, m, k = map(int, sys.stdin.readline().strip().split())
    
    # 배추밭
    arr = [[0] * m for _ in range(n)]
    # 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다.
    # 두 배추의 위치가 같은 경우는 없다.
    for i in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        arr[x][y] = 1
    
    print(arr)