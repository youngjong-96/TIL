# Python Functions

## 함수

: 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음

- 함수의 구조

```python
def <함수명>(매개변수1, 매개변수2, ... ):
		설명서(선택)
		실행 문장1
		실행 문장2
		...
		return <반환값>
```

- Sample

```python
def make_sum(num1, num2):       # num1, num2 는 매개변수
		"""이것은 두 수를 받아
		두 수의 합을 반환하는 함수입니다.
		>>> make_sum(1,2)
		3
		"""
		return num1 + num2
		
result = make_sum(3,4)           # 3, 4 는 인자
print(result)
```

- 함수는 return 만나면 종료~~~!!!! → return 문 아래에 있는 코드는 의미 없음~~~~~
- **함수 내에서 return 문이 없다면 None이 반환됨 (알아서 return None 추가함)**

<aside>
💡

출력(print) vs 반환(return)

**print( ) 함수는 return 값이 없음 (None 리턴) → 출력만 해주고 끝!**

</aside>

```python
value = print(1)  # 할당문으로 오른쪽 print 실행 후 value에 결과값(None) 할당
print(value)      # None 
>>> 1
    None
```

## 매개변수와 인자

- 인자의 종류
    1. **위치** 인자(Positional Arguments)
        - 함수 호출 시 반드시 전달해야 하고 없으면 TypeError 발생
    2. **기본** 인자 값(Default Argument Values)
        - 함수 정의에서 매개변수에 기본 값을 할당
        - 호출 시 전달 안하면 기본값 적용
    3. 키워드 인자(Keyword Arguments)
        - 함수 호출 시 인자의 이름과 함께 값을 전달
        - **호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함**
    4. **임의의** 인자 목록(Arbitrary Argument Lists) - “가변인자”
        - 정해지지 않은 개수의 인자를 처리하는 인자
        - 함수 정의 시 **매개변수 앞**에 `*` 를 붙여 사용
        - 여러 개의 인자를 tuple로 처리
    5. **임의의 키워드** 인자 목록(Arbitrary Keyword Argument Lists)  - “가변인자”
        - 함수 정의 시 **매개변수 앞**에 `**` 를 붙여 사용
        - 여러 개의 인자를 dictionary로 묶어 처리
    
    ```python
    def func(pos1, pos2, default_arg='default', *args, **kwargs):
    		print('pos1:', pos1)
    		print('pos2:', pos2)
    		print('default_arg:', default_arg)
    		print('args:', args)
    		print('kwargs:', kwargs)
    		
    func(1,2,3,4,5,6, key1='value1', key2='value')
    
    >>> pos1: 1
    		pos2: 2
    		default_arg: 3
    		args: (4,5,6)
    		kwargs: {'key1': 'value1', 'key2': 'value2'}
    ```
    

### 재귀 함수(recursion) : 함수 내부에서 자기 자신을 호출하는 함수

- 순서대로 모두 호출해서 쌓은 다음에 역순으로 계산

ex. 팩토리얼

```python
def factorial(n):
    # 종료 조건: n이 1이면 1을 반환
    if n == 1:
        return 1
    else:
        # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
        return n * factorial(n - 1)

# 팩토리얼 계산 예시
print(factorial(5))  # 120
```

- 특정 알고리즘 식을 표현할 때 변수 사용이 줄고 가독성이 높을 수 있지만, 메모리 사용이 많음
- 종료 조건을 잘못 설정하면 스택 오버플로우 발생

### 내장 함수(Built-in function) : 파이썬이 기본적으로 제공하는 함수

[https://docs.python.org/ko/3.12/library/functions.html](https://docs.python.org/ko/3.12/library/functions.html)

## 함수와 Scope

- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
    
    → 변수의 수명주기에 영향
    
- **이름 검색 규칙 (LEGB Rule)**
    - Local scope : 지역 범위
    - Enclosed scope : 지역 범위 한 단계 위 범위
    - Global scope : 최상단에 위치한 범위
    - Built-in scope : 모든 것을 담고 있는 범위
    
    안쪽(지역 범위)부터 바깥쪽으로 변수를 찾아감
    
    <aside>
    💡
    
    내장 함수명을 사용하면 다음부터 못 쓸 수 있음,,,
    
    </aside>
    
    ```python
    # 내장 함수 sum의 이름을 사용해버려서 오류가 발생하는 예시
    print(sum)  # <built-in function sum>
    print(sum(range(3)))  # 3
    sum = 5
    print(sum)  # 5
    print(sum(range(3)))  # TypeError: 'int' object is not callable
    ```
    
    ```python
    # LEGB Rule 퀴즈
    x = 'G'
    y = 'G'
    
    def outer_func():
        x = 'E'
        y = 'E'
    
        def inner_func(y):
            z = 'L'
            print(x, y, z)  # ??
    
        inner_func('P')
        print(x, y)  # ??
    
    outer_func()
    print(x, y)  # ??
    ```
    
    >>> E P L
    
       E E
    
       G G
    
    - 함수 정의와 호출하는 것 생각하기! inner_fuck는 p를 담아서 호출해서 결과가 예상과 다름
- global 키워드 : 함수 내에서 전역 변수 사용할 때
    - global 키워드 선언 전에 참조 불가
    - 매개변수에는 사용 불가

## 함수 스타일 가이드

- 소문자와 언더스코어(_) 사용
- 동사로 시작하여 함수의 동작 설명
- 약어 사용 지양
- True / False 를 반환한다면 is 또는 has 로 시작
- 단일 책임 원칙(Single Responsibility Principle) - 한 가지 함수는 한 가지 기

## Packing & Unpacking

- 패킹: 여러 개의 데이터를 하나의 컬렉션으로 모아 담는 과정, 주로 파이썬이 알아서 튜플로 묶음
    - *을 활용한 패킹 : 함수 정의에서 매개변수에 썼던 거 → 튜플로 묶임
    - **을 활용한 패킹 : 함수 정의에서 매개변수에 썼던 거 → 딕셔너리로 묶임
        
        (매개변수와 인자 파트 참고)
        
- 언패킹(시퀀스 언패킹, 다중 할당) : 컬렉션에 담겨 있는 요소들을 개별 변수에 할당
    - *을 활용한 언패킹 : 컬렉션 요소들을 하나씩 매개변수에 전달
    - **을 활용한 언패킹 : 컬렉션 키:값 쌍을 키=값 형태의 키워드 인자로 전달
        
        ```python
        # *, **을 활용한 언패킹 예시
        def my_function(a, b, c):
            print(a, b, c)
        
        my_list = [1, 2, 3]
        my_function(*my_list)  # 1 2 3 출력
        
        my_dict = {'a': 10, 'b': 20, 'c': 30}
        my_function(**my_dict) # 10 20 30 출력
        ```
        

| 구분 | 상황 | * 연산자 | ** 연산자 |
| --- | --- | --- | --- |
| 패킹 | 함수 정의 시 | 여러 위치 인자를 하나의 튜플로 받음 | 여러 키워드 인자를 하나의 딕셔너리로 받음 |
| 언패킹 | 함수 호출 시 | 리스트/튜플을 개별 위치 인자로 전달 | 딕셔너리를 개별 키워드 인자로 전달 |

## 참고

- 함수는 언제나 하나의 값만 반환 → 여러 값을 반환하면 하나의 튜플로 묶어서 반환 → 반환된 튜플을 언패킹해서 다시 사용
- lambda 표현식 : 일회용 함수 → 인자를 함수로 받는 함수에 유용하게 쓸 수 있음

```python
<함수명> lambda <매개변수> : <표현식(리턴값)>
```

## 핵심 키워드

| 개념 | 설명 | 예시 |
| --- | --- | --- |
| 함수(Function) | 재사용 가능한 코드 묶음 | def add(a, b): |
| 매개변수(Parameter) | 함수 정의 시 전달받는 변수 | def add(x, y): |
| 인자(Argument) | 함수 호출 시 전달하는 값 | add(a, b) |
| 재귀함수(Recursive) | 자기 자신을 호출하는 함수 | factorial(n-1) |
| 스코프(Scope) | 변수가 유효한 범위 | glabal num |
| LEGB 규칙 | 이름공간 탐색 순서 규칙 |  |
| 패킹(Paking) | 여러 값을 하나로 묶는 것 | *args |
| 언패킹(Unpacking) | 묶음을 여러 값으로 푸는 것 | a, b = my_tuple |
| 람다 표현식(Lambda) | 한 줄로 만드는 익명 함수 | lambda x: x**2 |