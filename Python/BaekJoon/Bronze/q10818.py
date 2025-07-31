# 최대, 최소 구하기
import sys

N = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

print(f"{min(num_list)} {max(num_list)}")