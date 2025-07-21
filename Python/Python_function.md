# [수치 연산 함수]
### 1. abs(): 인자로 숫자를 전달하면 그 숫자의 절대값을 반환
```
val = 10
print(abs(val))

>> 10
```

### 2. divmod() : 첫 번째 인자를 두 번째 인자로 나눴을 때의 몫과 나머지를 튜플 객체로 반환
```
print(divmod(9, 5))

>> (1, 4)   # 몫, 나머지
```

### 3. pow() : 첫 번째로 전달된 인자 값에 대해 두 번째로 전달된 인자 값으로 제곱한 결과를 반
```
data_list = [1, 2, 3, 4, 5]
print( list( map( lambda x: pow(x, 2), data_list)))

>> [1, 4, 9, 16, 25]
```

# [시퀀스형/반복 가능한 자료형을 다루는 함수]
### 4. all() 반복 가능한 자료형인 List, Tuple, Set, dictionary, 문자열 등을 인자로 전달하여 항목 모두가 True 이면 True, False가 하나라도 있으면 False
```
print( all( ['A', 'B', ""] ))

>> False
```

### 5. any() : 반복 가능한 자료형인 List, Tuple, Set, dictionary, 문자열 등을 인자로 전달하여 항목 모두가 False 이면 False, True가 하나라도 있으면 True
```
print( all( ['A', 'B', ""] ))

>> True
```

### 6. enumerate() : List, Tuple, 문자열과 같은 시퀀스형을 입력받아 인덱스를 포함하는 튜플 객체를 항목으로 구성하는 enumerate 객체를 반환
```
data_list = [10, 20, 30, 40, 50]

for obj in enumerate(data_list):
    print("{0}: {1}, {2}".format(type(obj), *obj))     #변수 obj: 인덱스와 값을 가진 튜플 객체를 {1}, {2}에 순서대로 대입

>> <class 'tuple'>: 0, 10
      <class 'tuple'>: 1, 20
      <class 'tuple'>: 2, 30
      <class 'tuple'>: 3, 40
      <class 'tuple'>: 4, 50
```

### 7. filter() : 조건에 해당하는 항목을 걸러내는 함수   filter(조건, 리스트)
```
def iseven(num):
    return num % 2 == 0

nubers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ret_val = filter(iseven, numbers)
 # ret_val = filter( lambda n: n%2 == 0, numbers)

print(type(ret_val))
print(list(ret_val))

>> <class 'filter'>
     [2, 4, 6, 8, 10]
```

### 8. list(), tuple(), set(), dict() : 반복 가능한 자료형을 인자로 전달 받아, 각각 리스트, 튜플, 셋, 딕셔너리로 변환해 반환
```
data_str = "Hello"

print(list(data_str))
>> ['H', 'e', 'l', 'l', 'o']

print(tuple(data_str))
>> ('H', 'e', 'l', 'l', 'o')

print(set(data_str))
>> {'H', 'e', 'l', 'o'}

print(dict(enumerate(data_str)))
>> {0: 'H', 1: 'e', 2: 'l', 3: 'l', 4: 'o'}
```

### 9. map() : 두 번째 인자로 반복 가능한 자료형을 전달 받아 자료형의 각 항목에 대해 첫 번째 인자로 전달 받은 함수를 적용한 결과를 맵 객체로 반환
```
[1]
data_list = list("abcdef")
result = list(map(lambda x: x.upper(), data_list))

print(result)

>> ['A', 'B', 'C', 'D', 'E', 'F']

[2]
var1, var2, var3 = map( int, input().split())
print(var1, var2, var3)

>> 1 2 3
     1 2 3
```

### 10. max(), min() : 반복 가능한 자료형을 인자로 전달받아 각각 항목 중 가장 큰 값, 작은 값 반환
```
data_list = list({10, 25, 30, 45, 50})

print("{0} => min: {1}, max: {2}".format(data_list,min(data_list),max(data_list)))

>> [10, 25, 30, 45, 50] => min: 10, max: 50
```

### 11. range() : (시작 값, 종료 값, 증감치)를 전달하여 시퀀스형 객체를 생성
```
data_list1 = list(range(0, 10, 1))
data_list2 = list(range(0, 10))
data_list3 = list(range(10))

print(data_list1)
print(data_list1)
print(data_list1)

>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 12. sorted() : 반복 가능한 자료형을 인자로 전달받아 항목들로부터 정렬된 리스트를 생성해 반환
```
data_list = [3, 8, 12, 2, 5, 11]
asc_result = sorted(data_list)
desc_result = list(reversed(asc_result))

print(asc_result)
print(desc_result)

>>  [2, 3, 5, 8, 11, 12]
      [12, 11, 8, 5, 3, 2]
```

### 13. zip() : 둘 이상의 반복 가능한 자료형을 인자로 전달받아, 동일 위치의 항목을 묶어 튜플을 항목으로 구성하는 zip 객체를 생성
 * 인자로 전달된 객체는 동일 자료형이면서, 항목의 개수가 같아야 함 

```
data_list1 = [1, 2, 3]
data_list2 = [4, 5, 6]
data_list3 = ["a", "b", "c"]


print(zip(data_list1, data_list2))
print(list(zip(data_list1, data_list2)))
>> <zip object at 0x0000027A80E91300>
      [(1, 4), (2, 5), (3, 6)]

print(list(zip(data_list1, data_list2, data_list3)))
>> [(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')]

print(dict(zip(data_list3, data_list1)))
>> {'a': 1, 'b': 2, 'c': 3}
```

# [변환 함수]
### 14. chr(), ord(), hex() :
정수 형태의 유니코드 값을 인자로 전달받아 해당 코드의 문자를 반환
문자를 인자로 전달받아 유니코드 값(10진 정수)을 반환
10진 정수 값을 인자로 전달받아 16진수로 변환된 값을 반환

```
print(chr(65))
>> A
print(ord('a'))
>> 97
print(ord('가'))
>> 44032
print(hex(ord('가')))
>> 0xac00
```

### 15. int(), float(), str()
인자로 전달된 숫자 형식의 문자열, 부동소수점 숫자를 정수로 변환
인자로 전달된 숫자 형식의 문자열, 정수를 부동소수점 숫자로 변환
인자로 전달된 객체에 대한 문자열 변환 값을 반환
```
x = "10" #문자열 10
y = "3C"
z = 4.5

print(int(x,  2))
>> 2   #2진수 10을 10진수 2로 변환 후 반환
print(int(y, 16))
>> 60  #16진수 3C를 10진수 60으로 반환
print(int(z))
>> 4   #버림
```

# [객체 조사를 위한 함수]
### 16. dir()
인자로 전달된 객체가 가지고 있는 변수, 메서드와 같은 속성 정보를 리스트 객체로 반환
인자를 전달하지 않고 호출하면 현재 지역 스코프에 대한 정보를 리스트 객체로 반환
```
print(dir())      #지역 스코프에 대한 정보를 리스트 객체로 반환
>> ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

data_str = "Hello, Python!"
print( dir(data_str))     #문자열이 가지고 있는 많은 메소드 정보를 리스트 객체에 담아 반환
>> ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

data_list = [10, 20, 30, 40, 50]
print( dir(data_list))      #정수형 리스트 객체가 가지고 있는 메소드 정보들을 리스트 객체에 담아 반환
>> ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

data_dict = {"key1" : 10, "key2" : 20, "key3" : 30}
print( dir(data_dict))      #객체가 가지고 있는 메소드 정보들을 리스트 객체에 담아 반환
>> ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
```

### 17. globals(), locals()
현재의 전역 심볼 테이블을 보여주는 딕셔너리를 반환
전역변수와 함수, 클래스의 정보 포함

현재의 지역 심볼 테이블을 보여주는 딕셔너리를 반환
매개변수를 포함한 지역변수와 중첩함수의 정보 포함
```
class MyClass:
      pass

def test_fn(param):
      def inner_fn():
              pass
      val1 = 5
      val2 = 8
      for item in locals().items():
            print(item[0], item[1])

value1 = 10
value2 = 20
obj1 = MyClass()

g = dict(globals())

print("globals()")
for item in g.items():
      print(item[0], item[1])

print("\n\nlocals()")
test_fn(10)


>>
globals()
__name__ __main__ __doc__ None __package__ None __loader__ <_frozen_importlib_external.SourceFileLoader object at 0x00000173B265BF20> __spec__ None __annotations__ {} __builtins__ <module 'builtins' (built-in)> __file__ c:\python\Quiz\s250715.py __cached__ None
MyClass <class '__main__.MyClass'> test_fn <function test_fn at 0x00000173B261CA40> value1 10 value2 20 obj1 <__main__.MyClass object at 0x00000173B285A660>

locals()
param 10 inner_fn <function test_fn.<locals>.inner_fn at 0x00000173B287D080> val1 5 val2 8
```


### 18. id() 인자로 전달된 객체의 고유 주소(참조값)를 반환
```
x = 10
print(hex(id(x)))
 >> 0x7ffc31fa4ad8

y = 10
print(hex(id(y)))
>> 0x7ffc31fa4ad8

z = "10"
print(hex(id(z)))
>> 0x1d6f9b89b00
```

### 19. isinstance(), issubclass()
첫 번째 인자로 전달된 객체가 두 번째 인자로 전달된 클래스의 인스턴스인지에 대한 여부를 T/F로 반환

첫 번째 인자로 전달된 클래스가 두 번째 인자로 전달된 클래스의 서브클래스인지에 대한 여부를 T/F로 반환
```
class Parent:
    pass

class Child(Parent):
    pass

p= Parent()
c = Child()

print(isinstance(p, Parent))
>>  True

print(isinstance(c, Child))
>> True

print(isinstance(c, Parent))
>>True
 
print(isinstance(p, Child))
>> False

print(issubclass(Child, Parent))
>> True
```

# [실행 관련 함수]
### 20. eval() : 표현 가능한 표현식의 문자열을 인자로 전달받아 해당 문자열의 표현식을 실행한 결과값을 반환
```
expr = "2 + 5 * 3"
expr2 = " 'hello, python!'.upper() "

print(eval(expr))
print(eval(expr2))

>>  17
       HELLO, PYTHON!
```