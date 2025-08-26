# 2xn 타일링
"""
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
"""
import sys

n = int(sys.stdin.readline().strip())

result = [0] * 1001
result[1] = 1
result[2] = 2

for i in range(3, n+1):
    result[i] = (result[i-2] + result[i-1]) % 10007

print(result[n])

