#정수가 몇 개 있는지 세기
import sys

N = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

V = int(sys.stdin.readline())

print(num_list.count(V))