#순서대로 별찍기(오른쪽 정렬)
import sys
T = int(sys.stdin.readline())

for i in range(T):
    print(" "*(T-(i+1)), end="")
    print("*"*(i+1))