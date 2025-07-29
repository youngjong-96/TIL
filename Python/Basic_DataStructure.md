# Data Structure

## 1. Data Structure

: 여러 데이터를 효과적으로 사용, 관리하기 위한 구조

- CS에서는 ‘**자료 구조**’라고 함
- 메서드 : 객체에 속한 함수, 클래스 내부에 정의되는 함수, 각 데이터 타입 별 다양한 기능을 가진 메서드가 존재
- 다양한 데이터 구조는 저마다 고유한 메서드를 가짐
    
    → 데이터를 효율적으로 조작하거나 특정 기능을 수행하기 위해
    
- 메서드 호출 방법
    
    ```python
    #데이터타입객체.메서드()
           "hello".capitalize()
    ```
    

## 2. 시퀀스 데이터 구조

### 문자열 조회/탐색 및 검증 메서드

| 메서드 | 설명 |
| --- | --- |
| s.find(x) | x의 첫 번째 위치를 반환, 없으면 -1 반환 |
| s.index(x) | x의 첫 번째 위치를 반환, 없으면 오류 반환(ValueError) |
| s.isupper() | 문자열 내의 모든 문자가 대문자인지 확인 |
| s.islower() | 문자열 내의 모든 문자가 소문자인지 확인 |
| s.isalpha() | 문자열 내의 모든 문자가 유티코드 상 문자인지 확인(한국어 포함) |

### 문자열 조작 메서드(새로운 문자열 반환) → 원본은 변경 x

| 메서드 | 설명 |
| --- | --- |
| **s.replace(old, new[,count])** | old 를 new 로 바꿔서 전환, 기본적으로 다바꿈, count에 숫자 넣으면 해당 개수만 바꿈 |
| **s.strip([chars])** | 공백이나 특정 문자([chars])를 제거
(단, 특정 문자는 양쪽 맨 끝에 있어야 함) |
| **s.split(sep=None, maxsplit=-1)** | sep를 구분자 문자열로 사용하여 문자열에 있는 단어들의 **리스트**를 반환
sep: 구분하는 기준
maxsplit: 최대 몇 번 자를건지 (1로 하면 첫 번째 구분자에서 한 번만 자름) |
| **'separator’.join(iterable)** | 구분자로 iterable의 **문자열**을 연결한 **문자열**을 반환 |
| s.capitalize() | 가장 첫 번째 글자를 대문자로 변경 |
| s.title() | 문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로, 나머지는 소문자로 반환 |
| s.upper() | 모두 대문자로 변경 |
| s.lower() | 모두 소문자로 변경 |
| s.swapcase() | 대문자 ↔ 소문자 서로 변경 |

```python
# replace()
text = 'Hello, world! world world'
new_text1 = text.replace('Hello','Python')    #일치하는거 다 바꿈
new_text2 = text.replace('Hello','Python', 1) #일치하는거 1개만 바꿈

print(new_text1)  # Hello, Python! Python Python
print(new_text2)  # Hello, Python! world world
```

```python
# strip
text1 = '  Hello, world!  '
text2 = 'Hello, world!  '
text3 = 'HHello, world!  '

new_text1 = text1.strip()      # 양쪽 공백 제거
new_text2 = text1.strip('H')   # 양쪽이 공백이여서 아무것도 제거 안 됨
new_text3 = text2.strip('H')   # 왼쪽에 H 제거
new_text4 = text3.strip('H')   # 왼쪽 H 2개 모두 제거

print(new_text1)  # Hello, world!
print(new_text2)  #   Hello, world!
print(new_text3)  # ello, world!
print(new_text4)  # ello, world!
```

```python
# join
words = ['Hello', 'world!']
new_text = '-'.join(words)
print(new_text)  # Hello-world!
```

<aside>
💡

1. **구분자로 사용할 문자열에서 호출**하는 독특한 형태를 가진다
    
    `구분자 . join` 
    
2. 요소는 반드시 **문자열**이어야 한다 (리스트를 요소로 넣지 않도록 주의!)
</aside>

```python
#리스트를 join 메서드의 요소로 활용하는 방법

numbers = [1, 2, 3, 4, 5]

# map() 사용
result_map = ','.join(map(str, numbers))
print(result_map)
# 출력: 1,2,3,4,5

# 리스트 컴프리헨션 사용
result_comp = ','.join([str(n) for n in numbers])
print(result_comp)
# 출력: 1,2,3,4,5
```

### 리스트 값 추가 및 삭제 메서드 → 원본을 직접 변경 → 반환값이 없음

| 메서드 | 설명 |
| --- | --- |
| **L.append(x)** | 리스트 마지막에 항목 x 를 추가 |
| **L.extend(m)** | iterable m의 모든 항목들을 리스트 끝에 추가 (+=과 같은 기능) |
| L.insert(i, x) | 리스트 인덱스 i에 항목 x를 삽입 |
| L.remove(x) | 리스트 가장 왼쪽에 있는 항목(첫 번째) x 를 제거
항목이 없으면 에러 반환 (ValueError) |
| **L.pop()** | 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거 |
| **L.pop(i)** | 리스트의 인덱스 i에 있는 항목을 반환 후 제거 |
| L.clear() | 리스트의 모든 항목 삭제 |

```python
# pop
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()       # 비워두면 맨 뒤값 반환, 반환값이 있음!
item2 = my_list.pop(0)      # 인덱스 지정 가능

print(item1)  # 5
print(item2)  # 1
print(my_list)  # [2, 3, 4]
```

### 리스트 탐색 및 정렬 메서드

| 문법 | 설명 |
| --- | --- |
| L.index(x) | 리스트에서 첫 번째로 일치하는 항목 x의 인덱스를 반환 |
| L.count(x) | 리스트에서 항목 x의 개수를 반환 |
| L.reverse() | 리스트의 순서를 역순으로 변경(**정렬x**)
’역순으로 정렬한다’ → 틀린 설명 |
| L.sort(reverse = False) | 원본 리스트를 오름차순으로 정렬(reverse = True 는 내림차순) |

## 3. 복사

### 가변과 불변 객체

- 가변과 불변 객체의 개념
    - 가변(Mutable) 객체 : 생성 후 내용을 변경할 수 있는 객체 (list, dict, set)
    - 불변(immutable) 객체 : 생성 후 내용을 변경할 수 없는 객체 (int, float, str, tuple)
- 파이썬에서 변수 할당 시 **새로운 객체**가 생성되거나 **기존 객체에 대한 참조**가 생성됨
- 가변/불변 메모리 관리 방식
    - 가변 객체 : 생성 후에도 그 내용을 수정할 수 있음, 객체의 내용이 변경되어도 같은 메모리 주소를 유지
    - 불변 객체 : 생성 후 그 값을 변경할 수 없음, 새로운 값을 할당하면 새로운 객체가 생성되고, 변수는 새 객체를 참조하게 됨
- 성능 최적화 관점
    - 가변 : 기존 객체를 직접 수정할 수 있어 객체 생성 및 삭제에 드는 비용을 절감
    - 불변 : 여러 변수가 동일한 객체를 안전하게 공유
- 메모리 효율성 관점
    - 가변 : 크기가 큰 데이터를 효율적으로 수정
    - 불변 : 동일한 값을 가진 여러 변수가 같은 객체를 참조할 수 있어 메모리 사용을 최소화

### 얕은 복사와 깊은 복사

- 얕은 복사 구현 방법
    - 리스트 슬라이싱 / copy( ) 메서드 / list( ) 함수
    
    ```python
    # 1차원 리스트에서의 얕은 복사 (리스트 슬라이싱)
    a = [1, 2, 3]
    b = a[:]
    
    print(a)  # [1, 2, 3]
    print(b)  # [1, 2, 3]
    
    # 1차원 리스트에서의 얕은 복사 (copy 메서드)
    a = [1, 2, 3]
    b = a.copy()
    
    print(a)  # [1, 2, 3]
    print(b)  # [1, 2, 3]
    
    # 1차원 리스트에서의 얕은 복사 (list() 함수)
    a = [1, 2, 3]
    d = list(a)
    a[0] = 100
    
    print(a)  # [100, 2, 3]
    print(d)  # [1, 2, 3]
    ```
    
    - 얕은 복사의 한계 → 1차원 리스트는 얕은 복사도 괜찮은데 다차원이 되니까 문제
    
    ```python
    # 얕은 복사의 한계
    print('\n다차원 리스트 얕은 복사의 한계')
    a = [1, 2, [3, 4, 5]]
    b = a[:]
    
    b[0] = 999
    print(a)  # [1, 2, [3, 4, 5]]
    print(b)  # [999, 2, [3, 4, 5]]
    
    b[2][1] = 100
    print(a)  # [1, 2, [3, 100, 5]]
    print(b)  # [999, 2, [3, 100, 5]]
    
    print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  # True
    ```
    
- 깊은 복사 : 중첩된 객체까지 모두 새로운 객체로 생성 → 복사본에 변경이 있어도 원복에 영향 없음
    - copy 모듈의 deepcopy 함수를 사용
    
    ```python
    # 깊은 복사
    import copy
    
    original = {
        'a': [1, 2, 3],
        'b': {'c': 4, 'd': [5, 6]},
    }
    copied = copy.deepcopy(original)
    
    copied['a'][1] = 100
    copied['b']['d'][0] = 500
    
    print(f'원본: {original}')  # {'a': [1, 2, 3], 'b': {'c': 4, 'd': [5, 6]}}
    print(f'복사본: {copied}')  # {'a': [1, 100, 3], 'b': {'c': 4, 'd': [500, 6]}}
    print(
        f"original['b']와 copied['b']가 같은 객체인가? {original['b'] is copied['b']}"
    )  # False
    ```
    

## 4. 참고

### List Comprehension

`[표현식 for 변수 in literable객체 if 조건]` 

```python
# List Comprehension 활용 예시
# "2차원 배열 생성 시 (인접행렬 생성 시)"
data1 = [[0] * (5) for _ in range(5)]
data2 = [[0 for _ in range(5)] for _ in range(5)]

>>>
"""
[[0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]]
"""
#data1 을 for 문으로 변경
data3 = []
for _ in range(5):
    data3.append([0]*5)

#data2 를 for 문으로 변경
data4 = []
for _ in range(5):
    temp_list = []
    data4.append(temp_list)
    for _ in range(5):
        temp_list.append(0)

```

### 메서드 체이닝

: 여러 메서드를 연속해서 호출하는 방식

<aside>
💡

잘못하면 `None.메서드를` 하는 상황이 발생해서 오류 날 수 있음 주의

(아래 리스트에서의 메서드 체이닝 잘못된 예시 참고)

</aside>

- 문자열에서의 메서드 체이닝

```python
# 문자열 메서드 체이닝
text = 'heLLo, woRld!'
new_text = text.swapcase().replace('l','z')
print(new_text)  # HEzzO, WOrLD!
```

- 리스트에서의 메서드 체이닝

```python
# 잘못된 체이닝 방식 1
numbers = [3, 1, 4, 1, 5, 9, 2]
result = numbers.copy().sort()
print(numbers)  # [3, 1, 4, 1, 5, 9, 2] (원본은 변경되지 않음)
print(result)  # None (sort() 메서드는 None을 반환하기 때문)

# 잘못된 체이닝 방식 2
result = numbers.append(7).extend([8, 9])  # AttributeError

# 개선된 방식
# 필요한 경우 새로운 리스트 객체를 반환하는 함수를 사용하는 것이 좋음
sorted_numbers = sorted(numbers.copy())
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 9]
```

<aside>
💡

sorted( ) : 내장함수

L.sort( ) : 리스트 메서드

</aside>

### 문자 유형 판별 메서드

- isdecimal( ) : 문자열이 모두 일반적인 십진수 숫자 0~9만 있는지
- isdigit( ) : 일반 숫자뿐만 아니라 지수 표현, 유니코드 숫자도 숫자로 인식
- isnumeric( ) : isdigit( )에서 분수, 지수, 루트 기호도 숫자로 인식

## 5. 핵심 정리

### 확인 문제

1. 다음 코드 실행 후 orig의 출력 결과는?

```python
orig = [1, [2,3]]
shallow = orig[:]

shallow[1].append(4)
print(orig)
```

>>> [1,[2,3,4]]

오류 나거나 [1,[2,3],4] 이런 형태로 들어가지 않고 [2,3]리스트 안에 들어감

1. 다음 코드 실행 후 list1의 출력 결과로 옳은 것은?

```python
list1 = [1,2]
list2 = list1
list2.append(3)
print(list1)
```

>>> [1,2,3]

list2 가 가리키는 객체와 list1이 가리키는 객체가 동일하게 되어 list1도 함께 변경된다

### 핵심 키워드

| 개념 | 설명 |
| --- | --- |
| 자료 구조 (Data Structure) | 데이터를 효율적으로 저장, 관리하기 위한 형식 |
| 시퀀스 (Sequence) | 순서를 유지하고 인덱스로 접근 가능 |
| 문자열 (str) | 불변 문자 시퀀스 |
| 리스트 (list) | 순서가 있고 가변인 시퀀스 |
| 불변 객체 (immutable) | 내부 값 변경 불가, 연산 시 새 객체 생성 |
| 가변 객체 (Mutable) | 내부 값 직접 변경, 참조는 유지 |
| 얕은 복사 (Shallow Copy) | 최상위만 새 메모리, **내부 객체는 참조 공유** |
| 깊은 복사 (Deep Copy) | 모든 중첩 레벨까지 새 겍체 생성 |
| 리스트 컴프리헨션 | [표현식 for 변수 in iterable if 조건식] 형식으로 효율적 리스트 생성 |
| 메서드 체이닝 | 객체를 반환하는 메서드를 연속 호출 |




## 비시퀀스 데이터 구조

### 딕셔너리 : 키와 값을 짝지어 저장하는 자료구조

- 딕셔너리는 내부적으로 해시테이블을 사용하여 키-값 쌍을 관리
- 키를 통한 값의 삽입, 삭제, 검색이 데이터의 크기와 관계없이 매우 빠름
- 키는 고유값, 값은 중복이 가능하고 어떤 자료형도 가능

딕셔너리 메서드

| 메서드 | 설명 |
| --- | --- |
| D.get(k[,default]) | 키로 값을 반환, 키가 없으면 None 혹은 [default]에 넣은 값을 반환
- D[key]한 것과 동일한 결과지만 [ ]로 값을 조회할 때 값이 없으면 KeyError 발생 |
| D.keys( ) | 딕셔너리 키를 모은 **객체**를 반환, iterable 로 순회 가능
실시간으로 동기화되는 확인 창(view) → 변경사항 바로 반영 |
| D.values( ) | 딕셔너리 값을 모든 **객체**를 반환, iterable 로 순회 가능 |
| D.items( ) | 딕셔너리 키/값 쌍을 모은 객체를 반환, iterable 로 순회 가능 |
| D.pop(k[, default]) | 키를 제거하고 값을 반환, 키가 없으면 KeyError 혹은 [default]에 넣은 값을 반환 |
| D.clear( ) | 딕셔너리의 모든 키/값 쌍을 제거 |
| D.setdefault(k[, default]) | 키와 연결된 값을 반환, 키가 없으면 default와 연결한 키를 딕셔너리에 추가하고 default를 반환
- 키가 이미 있으면 default 값을 넣어줘도 기존의 값 출력함 |
| D.update(*[other]*) | other 가 제공하는 키/값 쌍으로 딕셔너리를 갱신하고 기존 키는 덮어씀 |
- get

```python
# get
person = {'name': 'Alice', 'age': 25}
print(person.get('name'))   # Alice
print(person.get('country', '해당 키는 존재하지 않습니다.'))  # 해당 키는 존재하지 않습니다
# print(person['country'])  # KeyError: 'country'
```

- pop

```python
# pop
person = {'name': 'Alice', 'age': 25}
print(person.pop('age'))  # 25
print(person)  # {'name': 'Alice'}
print(person.pop('country', None))  # None
# print(person.pop('country'))  # KeyError: 'country'
```

- update

```python
# update
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'country': 'KOREA'}

person.update(other_person) # person 딕셔너리에 other_person 딕셔너리를 덮어씀
print(person)  # {'name': 'Jane', 'age': 25, 'country': 'KOREA'}

person.update(age=100, address='SEOUL') # person 딕셔너리에 키:값 쌍 추가
print(person)  # {'name': 'Jane', 'age': 100, 'country': 'KOREA', 'address': 'SEOUL'}
```

### Set : 고유한 항목들의 정렬되지 않은 컬렉션

- Set은 내부적으로 해시 테이블을 사용하여 데이터를 저장
- 항목의 고유성을 효율적으로 보장, 항목의 추가, 삭제, 존재 여부 확인이 데이터의 크기에 관계없이 매우 빠르다
- 합집합, 교집합, 차집합 등 수학적인 집합 연산을 수행할 수 있음

세트 메서드

| 메서드 | 설명 |
| --- | --- |
| s.add(x) | 세트에 x 를 추가 |
| s.update(iterable) | 세트에 다른 iterable 요소를 추가 (이미 있는 건 안들어감)
- iterable 을 안 넣으면 TypeError 발생 |
| s.clear( ) | 세트의 모든 항목을 제거 |
| s.pop( ) | 세트에서 **임의의(무작위 x)** 요소를 제거하고 반환
- 해쉬함수가 버킷 위치를 임의로 배치한 후 찾아감으로 random은 아니지만 임의의 요소를 제거한다 |
| s.remove(x) | 세트에서 항목 x를 제거 , 항목 x가 없을 경우 keyError 발생 |
| s.discard(x) | 세트에서 항목 x를 제거, remove와 달리 에러 없고 아무것도 출력하지 않음 |

세트 집합 메서드

| 메서드 | 설명 | 연산자 |
| --- | --- | --- |
| set1.difference(set2) | 차집합 | set1 - set2 |
| set1.intersection(set2) | 교집합 | set1 & set2 |
| set1.issubset(set2) | set1 이 포함되는가 | set1 ≤ set2 |
| set1.issuperset(set2) | set1 이 포함하는가 | set1 ≥ set2 |
| set1.union(set2) | 합집합 | set1 | set2 |

```python
# 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2))  # {0, 2, 4}
print(set1.intersection(set2))  # {1, 3}
print(set1.issubset(set2))  # False
print(set3.issubset(set1))  # True
print(set1.issuperset(set2))  # False
print(set1.union(set2))  # {0, 1, 2, 3, 4, 5, 7, 9}
```

## 참고

### 해시 테이블

: ‘키’와 ‘값’을 짝지어 저장하는 자료구조

- 해시(Hash) : 임의의 크기를 가진 데이터를 고정된 크기의 고유한 값으로 변환하는 것
- 해시 함수 : 임의 길이 데이터를 입력 받아 고정 길이(정수)로 변환해 주는 함수
    - 해시 함수는 키를 입력받아 데이터를 저장하거나 찾을 배열의 정확한 인덱스를 즉시 계산
    
    <aside>
    💡
    
    해시 함수 결과로 정수를 반환하기 때문에 입력을 정수로 하면 단순 계산으로 고정됨
    
    문자열은 항상 달라짐 - 난수 시드(seed)가 달라지기 때문
    
    </aside>
    
    ```python
    # 정수
    my_set = {3, 2, 1, 9, 100, 4, 87, 39, 10, 52}
    print(my_set.pop())
    print(my_set.pop())
    print(my_set.pop())
    print(my_set.pop())
    print(my_set.pop())
    print(my_set.pop())
    print(my_set.pop())
    print(my_set.pop())
    print(my_set.pop())
    print(my_set.pop())
    print(my_set)
    
    >>>
    1
    2
    3
    100
    4
    39
    9
    10
    52
    87
    set()       # 실행할 때마다 동일
    ```
    
    ```python
    # 문자열
    my_str_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
    print(my_str_set.pop())
    print(my_str_set.pop())
    print(my_str_set.pop())
    print(my_str_set.pop())
    print(my_str_set.pop())
    
    >>>
    g
    a
    b
    f
    j           # 실행할 때마다 다름
    ```
    
    ```python
    print(hash(1))           # 1    (실행 때마다 동일)
    print(hash(1.0))         # 1    (실행 때마다 동일)
    print(hash('1'))         # -9019818709412715630   (실행 때마다 다름)
    print(hash((1, 2, 3)))   # 529344067295497451     (실행 때마다 다름)
    ```
    
- 해시 테이블의 원리
    1. 키를 해시 함수를 통해 해시 값으로 변환
    2. 변환된 해시 값을 인덱스로 삼아 데이터를 저장하거나 찾음
    3. 이로 인해 검색, 삽입, 삭제를 매우 빠르게 수행
- set의 요소 & dict의 키와 해시 테이블 관계
    - set
        - 각 요소를 해시 함수로 변환해 나온 해시 값에 맞춰 해시 테이블 내부 버킷에 위치
        - 버킷위치(인덱스)가 요소의 위치를 결정
        - 따라서 set는 순서를 보장하지 않음
    - dict
        - 키 → 해시 함수 → 해시 값 → 해시 테이블에 저장
        - 단 set와 달리 삽입 순서는 유지한다는 것이 언어 사양에 따라 보장 됨 (python 3.7 이상)
            - 키를 추가한 순서대로 반복문 순회할 때 나오게 됨
            - 사용자에게 보여지는 키 순서는 삽입 순서가 유지되도록 설계된 것 → 순서는 없음
- 대부분의 불변 타입은 해시 가능하고 가변형 객체는 기본적으로 해시 불가능

```python
print(hash((1, 2, [3, 4]))) # TypeError: unhashable type: 'list'
print(hash([1, 2, 3])) # TypeError: unhashable type: 'list'
my_set = {[1, 2, 3], 1, 2, 3, 4, 5} # TypeError: unhashable type: 'list'
# set 에 리스트를 넣을 수 없다 (가변형 자료를 set에 넣을 수 없다)
my_dict = {{3, 2}: 'a'} # TypeError: unhashable type: 'set'
# dict 의 키로 set를 넣을 수 없다
print(hash({'word','abc'})) # TypeError: unhashable type: 'set'
```

- hashable(해시가 가능한 객체) 객체가 필요한 이유
    - 해시 테이블 기반 자료 구조 사용
    - 불변성을 통한 일관된 해시 값
    - 안정성과 예측 가능성 유지

### 파이썬 문법 규격

- 대표적인 EBNF 메타기호
    - [ ] : 선택적 요소
    - { } : 0번 이상 반복
    - ( ) : 그룹화
- BNF와 같은 표기법을 사용하는 이유
    - 서로 다른 프로그래밍 언어, 데이터 형식, 프로토콜 등의 문법을 통일하여 정의하기 위함


## 핵심요약

| 개념 | 설명 |
| --- | --- |
| 딕셔너리 (Dictionary) | 고유한 키-값 쌍을 저장하는 비시퀀스 컬렉션 |
| 세트 (Set) | 중복을 허용하지 않는 정렬 되지 않은 컬렉션 |
| 해시 테이블(Hash Table) | 키를 해시 값으로 변환해 배열 인덱스로 사용해 빠른 검색-삽입-삭제를 지원 |
| hashable (해시 가능) | 내부 값이 변하지 않아 동일한 해시 값을 유지하는 객체만 dict 키, set 요소로 사용 가능 |
| 집합 연산 | 두 세트의 합집합, 교집합, 차집합 등을 통해 중복 제거와 관계 분석 수행 |
| dict.get( ) | 키가 없을 때 기본값을 반환해 안전하게 조회할 수 있는 메서드 |
| 키 (Key) | 값에 접근하기 위한 고유 식별자 - 인덱스 대신 사용돼 가독성과 검색 속도를 향상 |
| EBNG 메타기호 [ ] | 공식 문서에서 선택적 매개변수를 나타내는 표기법 (대괄호 안은 선택) |