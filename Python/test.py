# 1. 단일 튜플에 후행쉼표를 쓰지 않으면?
tuple1 = (1,)
tuple2 = (1)

print(type(tuple1))   # <class 'tuple'>
print(type(tuple2))   # <class 'str'>


# 2. range()는 추가적인 명령이 없으면 우선 규칙만 기억한다
print(range(1,11))    # range(1, 11)


# 3. range()에서 시작값과 끝 값이 이상하게 설정되면 빈 값이 나온다
print(list(range(4,1)))       # []
print(list(range(1,4,-1)))    # []
print(range(4,1))             # range(4, 1)


# 4. set 에서 사용되는 집합연산자도 복합연산자로 사용이 가능할까? -> YES
set1 = {1,2,3}
set2 = {3,4,5}

set1 &= set2   #set1 = set1 & set2
print(set1)    # {3}


# 5. is 와 ==
print(2 is 2.0)  # False
print(2 == 2.0)  # True

# 6. 반환값이 없는 함수 주의
def func(args):
    print(args)

result = func("hello")
print(result)   # None

# >>> hello
#     None


# 7. 내장함수를 변수명으로 사용하는 경우 -> 오류 발생
sum = 5
print(sum)
# print(sum(range(3)))  # TypeError: 'int' object is not callable


# 8. LEGB Rule
x = 'G'
y = "G"

def outer_func():
    x = 'E'
    y = 'E'
    def inner_func(y):
        z = 'L'
        print(x,y,z)  # E P L
    inner_func('P')
    print(x, y)  # E E

outer_func()
print(x,y) # G G


# 9. zip() 함수 - iterable을 같은 위치끼리 모아서 반환
scores = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

for score in zip(*scores):
    print(score)

# >>>
"""
(1, 4, 7)
(2, 5, 8)
(3, 6, 9)
"""


# 10. 


