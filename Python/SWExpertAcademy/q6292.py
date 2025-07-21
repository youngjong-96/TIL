#콤마(,)로 구분된 정수 값을 입력받아 리스트와 튜플 객체를 생성하는 코드를 작성하십시오.
import sys
list1 = list(map(int, sys.stdin.readline().split(','))) 
print(list1)
print(tuple(list1))
