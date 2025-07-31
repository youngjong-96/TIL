# OOP

## 프로그래밍 패러다임

### 1. 절차 지향 프로그래밍

: 함수와 로직 중심 작성, 데이터를 순차적으로 처리

```python
# 절차 지향 사고
# 예: 변수와 함수를 별개로 다룸
name = 'Alice'
age = 25

def introduce(name, age):
    print(f'안녕하세요, {name}입니다. 나이는 {age}살입니다.')

introduce(name, age)

>>> 안녕하세요, Alice입니다. 나이는 25살입니다.
```

- 입력 받고, 처리하고, 결과를 내는 과정이 아래로 순차적으로 흐름
- 데이터와 함수의 분리
- 함수 호출의 흐름이 중요
- 절차 지향적 프로그래밍의 한계
    - 복잡성 증가
    - 유지보수 문제

### 2. 객체 지향 프로그래밍

: 클래스는 설계도, 인스턴스는 실제 물건

```python
# 객체 지향 사고
# 예: 사람(객체) 안에 name, age와 이와 관련된 기능(메서드) 포함
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'안녕하세요, {self.name}입니다. 나이는 {self.age}살입니다.')

alice = Person('Alice', 25)
alice.introduce()  # 객체가 자신의 정보를 출력

>>> 안녕하세요, Alice입니다. 나이는 25살입니다.
```

- 데이터(변수)와 그 데이터를 처리하는 함수(메서드)를 하나의 단위(객체)로 묶어서 관리
- 객체 = 데이터(변수) + 메서드(함수)

<aside>
💡

절차 지향에서는 데이터가 함수의 매개변수로 전달되어 처리되는 수동적 존재였지만, 객체 지향에서는 데이터와 해당 데이터를 처리하는 메서드가 하나의 객체로 통합되어 스스로 기능을 수행하는 능동적 존재가 되었다

→ 코드의 구조화와 재사용성을 높이고, 실제 세계의 모델링 방식과 더 유사한 프로그래밍을 가능하게 한다

</aside>

<aside>
💡

절차 지향과 객체 지향은 대조되는 개념이 아니다

→ 객체 지향은 기존 절차 지향을 기반으로 객체라는 개념으로 보완한 개념

→ 객체 지향은 상속, 코드 재사용성, 유지보수성 등의 이점을 가진다

</aside>

### 3. 객체와 클래스

- 객체 : 실제 존재하는 사물을 추상화한 것. 속성과 동작(메서드)을 가짐, 독립적이다(고유성을 가짐)
- 클래스 : 객체를 만들기 위한 설계도, 파이썬에서 타입을 표현하는 방법, 하나의 구조 안에 데이터(변수)와 기능(함수)을 함께 정의하는 도구

## 클래스 기초

### 1. 클래스

- 클래스 이름은 파스칼 케이스(Pascal Case; 첫글자 대문자 이후 단어조합 시 첫글자 대문자) 방식으로 작성

```python
class Person:
    # 생성자 메서드
    def __init__(self, name, age):
            # 인스턴스 속성
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f'안녕하세요. 저는 {self.name}, 나이는 {self.age}살입니다.')
```

### 2. 인스턴스

: 클래스를 통해 생성된 객체, 한 클래스로 여러 인스턴스를 만들 수 있으며, 각 인스턴스는 서로 독립된 데이터를 가진다

```python
# 클래스 정의
class Person:
    def __init__(self, name, age):
        self.name = name  # 인스턴스 속성
        self.age = age  # 인스턴스 속성

    def introduce(self):
        print(f'안녕하세요. 저는 {self.name}, 나이는 {self.age}살입니다.')

# 인스턴스 생성
p1 = Person('Alice', 25)   # 인스턴스 생성
print(p1.name)             # 인스턴스 변수 접근 및 출력
p1.introduce()             # 메서드 호출
p2 = Person('Bella', 22)
print(p2.name)
p2.introduce()

>>>
Alice
안녕하세요. 저는 Alice, 나이는 25살입니다.
Bella
안녕하세요. 저는 Bella, 나이는 22살입니다.
```

### 3. 클래스와 인스턴스

- 클래스를 정의한다는 것은 공통된 특성과 기능을 가진 틀을 만드는 것
- 공통된 특성과 기능을 가진 틀을 만드는 것은 곧 새로운 타입을 만드는 행위

```python
name = 'Alice'

# 변수 name 은 str 클래스의 인스턴스이다.
```

### 4. 클래스 구성요소

- 생성자 메서드
    - 인스턴스 생성 시 자동 호출되는 메서드
    - `__init__` 이라는 이름으로 정의
    - 인스턴스 변수 초기화 담당
- 인스턴스 변수(속성)
    - 인스턴스별 고유 속성
    - self.변수명 형태로 정의
    - 인스턴스마다 독립적인 값 유지
- 클래스 변수(속성)
    - 모든 인스턴스가 공유하는 속성
    - 클래스 내부에서 직접 정의

```python
class Circle:
    pi = 3.14
    # 생성자 메서드
    def __init__(self, radius):
        # 인스턴스 변수(속성)
        self.radius = radius

# 인스턴스 생성
c1 = Circle(1)
c2 = Circle(2)

# 인스턴스 변수(속성) 접근
print(c1.radius)
print(c2.radius)

# 클래스 변수(공통 속성) 접근
print(c1.pi)
print(c2.pi)

>>>
1
2
3.14
3.14
```

### 5. 클래스 변수와 인스턴스 변수

- 클래스 변수와 동일한 이름으로 인스턴스 변수 생성 시, 인스턴스 변수 먼저 참조함

```python
class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

c1 = Circle(5)

# c1이 본인 인스턴스 변수 pi를 생성
c1.pi = 100

print(c1.pi) # 100
```

## 메서드 : 클래스 내부에 정의된 함수

### 1. 인스턴스 메서드

: 인스턴스의 상태를 조작하거나 동작을 수행, 인스턴스마다 독립적으로 행동할 수 있게 만드는 것

- 클래스 내부에 정의되는 메서드의 기본
- 반드시 첫 번째 인자로 인스턴스 자신(self)을 받음
- 인스턴스의 속성에 접근하거나 변경 가능
- self 동작 원리 - 인스턴스 메서드의 첫번째 인자가 반드시 인스턴스 자기 자신인 이유
    
    ```python
    'hello'.upper()
    # 파이썬 내부 동작은 아래와 같이 진행
    # str.upper('hello')
    # str 클래스가 upper 메서드를 호출하고, 그 첫번째 인자로 문자열 인스턴스가 들어감
    ```
    
    ‘hello’.upper( ) 은 str.upper(’hello’)를 객체 지향 방식의 메서드로 호출하는 표현(단축형 호출)
    
    ‘hello’ 라는 문자열 객체가 스스로 메서드를 호출하여 코드를 동작하는 객체 지향적인 표현인 것
    

```python
class Counter:
        # 생성자 메서드
    def __init__(self):
        self.count = 0

    # 인스턴스 메서드
    def increment(self):
        self.count += 1

# 인스턴스 생성
c = Counter()
# 인스턴스 메서드 호출
c.increment()
print(c.count)   # 1
```

생성자 메서드 동작 참고

```python
class Person:
    # 생성자 메서드
    def __init__(self, name):
        self.name = name
        print("인스턴스가 생성되었습니다.")

    def greeting(self):
        print(f'안녕하세요 {self.name}입니다.')

person1 = Person("지민")
person1.greeting()       # 안녕하세요 지민입니다.
Person.greeting(person1) # 안녕하세요 지민입니다.
```

### 2. 클래스 메서드

: 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행, `@classmethod` 를 사용

- 클래스 메서드 구조
    - 호출 시, 첫번째 인자로 해당 메서드를 호출하는 클래스(cls)가 전달됨
    - 클래스를 인자로 받아 클래스 속성을 변경하거나 읽는 데 사용

```python
class Person:
        # 클래스 변수
    population = 0
    
        # 생성자 메서드
    def __init__(self, name):
        self.name = name
        Person.increase_population()  # 인스턴스 생성 시 클래스 매서드 호출

    # 클래스 메서드
    @classmethod
    def increase_population(cls):
        cls.population += 1

# 인스턴스 생성
person1 = Person('Alice')
person2 = Person('Bob')

# 클래스 변수 접근
print(Person.population)  # 2
```

### 3. 스태틱 메서드

: 클래스, 인스턴스와 상관없이 독립적으로 동작하는 메서드, `@staticmethod` 사용

- 스태틱 메서드 구조
    - 호출 시 자동으로 전달 받는 인자가 없음

```python
class MathUtils:
    # 정적 메서드
    @staticmethod
    def add(a, b):
        return a + b

# 정적 메서드 호출
print(MathUtils.add(3,5))  # 8
```

### 4. 메서드 활용

은행 계좌 조작하는 클래스 만들기 실습

```python
# 입출금이 가능한 은행 계좌 클래스 만들기
# 은행 계좌를 모델링하는 클래스를 만들고, 입출금 기능(메서드)를 구현

class BankAccount:
    interest_rate = 0.02
    
    # 생성자 메서드
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    # 입금
    def deposit(self, amount):
        self.balance += amount

    # 출금
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("잔액이 부족합니다.")

    # 이자율 설정
    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate

    # 계좌 잔액이 양수인지 확인
    @staticmethod
    def is_positive(amount):
        return amount > 0

# 계좌 개설 (인스턴스 생성)
alice_acc = BankAccount("Alice", 1000)

# 입금 및 출금 (인스턴스 메서드 호출)
alice_acc.deposit(500)
alice_acc.withdraw(200)

# 잔액 확인 (인스턴스 변수 참조)
print(alice_acc.balance)

# 이자율 변경 (클래스 메서드 호출)
BankAccount.set_interest_rate(0.03)  # 이자율 변경 0.02 -> 0.03
print(BankAccount.interest_rate)

# 잔액이 양수인지 확인 (정적 메서드 호출)
print(BankAccount.is_positive(alice_acc.balance))

>>>
1300
0.03
True
```

### 5. 메서드 정리

- 클래스가 사용해야 할 것 (하지만 클래스에서 모든 메서드를 호출할수는 있음)
    - 클래스 메서드
    - 스태틱 메서드
- 인스턴스가 사용해야 할 것 (하지만 인스턴스에서 모든 메서드를 호출할수는 있음)
    - 인스턴스 메서드

## 참고

### 1. 클래스와 인스턴스 간 이름 공간

- 속성 접근 시 인스턴스 → 클래스 순서로 탐색됨 → 같은 이름의 속성이 중복되면 인스턴스 값 우선
- 독립적인 이름공간을 가지는 이점
    - 서로의 데이터나 상태에 직접적인 접근이 불가능
    - 각가의 객체가 독립적으로 동작하도록 보장
    - 서로 충돌하지 않음
    - 가독성, 유지보수성, 재사용성을 높임

### 2. 매직 메서드

- 특정 상황에 자동으로 호출됨
- 인스턴스 메서드
- 매직 메서드 `__str__`
    - print 로 호출할 때, 내가 지정한 형식으로 호출되도록 하는 메서드
    - print 로 인스턴스 출력할 때 (생성자 메서드가 인스턴스 생성 때 자동 실행되는 것처럼) 자동 실행
    
    ```python
    class Circle:
        def __init__(self, radius):
            self.radius = radius
    
        # __str__ 메서드 정의
        # 인스턴스를 문자열로 표현할 때 호출됨
        # print(c1) 호출 시 사용됨
        # 이 메서드를 정의하면 인스턴스를 print()로 출력할 때 더 읽기 쉬운 형식으로 출력됨
        # __str__ 메서드는 문자열을 반환해야 함
        def __str__(self):
            return f'원의 반지름: {self.radius}'
    
    c1 = Circle(10)
    c2 = Circle(1)
    
    print(c1)  # 원의 반지름: 10
    print(c2)  # 원의 반지름: 1
    ```
    

### 3. 데코레이터

: 다른 함수의 코드를 유지한 채로 수정하거나 확장하기 위해 사용되는 함수

```python
# 데코레이터 정의
def my_decorator(func):
    def wrapper():
        # 함수 실행 전에 수행할 작업
        print('함수 실행 전')
        # 원본 함수 호출
        result = func()
        # 함수 실행 후에 수행할 작업
        print('함수 실행 후')
        return result

    return wrapper

# 데코레이터 사용
@my_decorator
def my_function():
    print('원본 함수 실행')

my_function()

>>>
함수 실행 전
원본 함수 실행
함수 실행 후
```


## 상속

### 1. 클래스 상속

### 상속 : 한 클래스(부모)의 속성과 메서드를 다른 클래스(자식)가 물려받는 것

- 속성과 메서드를 자식에게 넘겨주는 과정
- 상속이 필요한 이유
    - 코드 재사용, 계층 구조로 관계를 표현, 유지 보수의 용이성

```python
# 상속 기본 예시
class Animal:
    def eat(self):
        print('먹는 중')

class Dog(Animal):
    def bark(self):
        print('멍멍')
        
my_dog = Dog()
my_dog.bark()  # 멍멍

# 부모 클래스(Animal) 메서드 사용 가능
my_dog.eat()  # 먹는 중
```

```python
# 상속을 사용한 계층구조 변경
# Person 클래스를 Professor 와 Student 가 각각 상속 받아 활용
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):  # 메서드 재사용
        print(f'반갑습니다. {self.name}입니다.')

class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

# 부모 Person 클래스의 talk 메서드를 활용
p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

# 부모 Person 클래스의 talk 메서드를 활용
p1.talk()   # 반갑습니다. 박교수입니다.
s1.talk()   # 반갑습니다. 김학생입니다.
```

### 2. 메서드 오버라이딩

: 부모 클래스의 메서드를 같은 이름, 같은 파라미터 구조로 재정의하는 것

- 자식 클래스에서 매서드를 다시 정의해서 기능을 유지하면서도 일부 동작을 맞춤형으로 바꾸고 싶을 때 유용
- 오버라이딩은 동일한 이름과 매개변수를 사용

```python
# 오버라이딩 예시
class Animal:
    def eat(self):
        print('Animal이 먹는 중')

class Dog(Animal):
    # 오버라이딩 (부모 클래스 Animal의 eat 메서드를 재정의)
    def eat(self):
        print("Dog가 먹는중")

my_dog = Dog()
my_dog.eat()  # Dog가 먹는 중
```

- 근데 동일한 이름으로 매개변수를 추가한다면?!

```python
class Dog(Animal):
    # 오버라이딩 (부모 클래스 Animal의 eat 메서드를 재정의)
    def eat(self, food):
        print(f"Dog가 {food}를 먹는중")

my_dog = Dog()
my_dog.eat('사료')  # Dog가 사료를 먹는중
```

- 된다!!!
- 하지만 동일한 매개변수를 사용하도록 추천하는 이유는 “다형성”을 위반하지 않기 위함

```python
# 잘못된 오버라이딩의 위험성 예시

class Animal:
    def eat(self):
        print('Animal이 먹는 중')

class Dog(Animal):
    # 잘못된 오버라이딩: 부모와 파라미터 구조가 다름
    def eat(self, food):
        print(f'Dog가 {food}를 먹는 중')

class Cat(Animal):
    # 올바른 오버라이딩: 부모와 파라미터 구조가 같음
    def eat(self):
        print('Cat이 조용히 먹는 중')

# 동물들에게 밥을 주는 함수 (다형성 활용)
def feed_animal(animal):
    # 이 함수는 animal 객체에 eat() 메서드가 있을 것이라고 기대함
    animal.eat()

# 객체 생성
dog = Dog()
cat = Cat()

feed_animal(cat)  # 문제 없이 실행됨
feed_animal(dog)  # TypeError 발생
```

- `feed_animal` 함수는 `dog` 객체 또한 `Animal`의 일종이므로 당연히 `eat()`를 호출할 수 있을 것이라 예상했지만, `Dog` 클래스가 `eat` 메서드를 `food`라는 추가 파라미터가 필요한 메서드로 덮어썼기 때문에 `TypeError`가 발생
- 이처럼 자식 클래스가 부모 클래스의 메서드 시그니처(이름과 파라미터 구조)를 임의로 변경하면, 부모 타입으로 객체를 다루는 코드에서 더 이상 해당 자식 객체를 안전하게 사용할 수 없게 됨

<aside>
💡

파이썬은 오버로딩 지원하지 않음!

파이썬에서는 같은 이름, 다른 파라미터로 함수 정의하면 마지막만 기억함

- 오버로딩: 같은 이름, 다른 파라미터를 가진 여러 메서드를 정의하는 것
</aside>

### 3. 다중 상속

: 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속 받는 것

- 상속 받는 모든 클래스의 요소를 활용 가능하다
- 중복된 속성이나 메서드가 있으면 상속 순서에 의해 결정된다

```python
# 다중 상속 예시
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'

class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'

class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'

class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'

baby1 = FirstChild('name')
print(baby1.cry())  # 첫째가 응애
print(baby1.swim())  # 첫째가 수영
print(baby1.walk())  # 아빠가 걷기
print(baby1.gene)  # XY
```

- 다이아몬드 문제 : 한 클래스가 두 개의 클래스를 상속 받을 때 어느 것을 선택하냐의 문제
    - 파이썬에서의 해결책 : MRO(Method Resolution Order) 알고리즘을 사용하여 클래스 목록을 생성
        - 부모 클래스로부터 상속된 속성을 정해진 내부 알고리즘에 따라 검색
        - 이 순서는 기본적으로 왼쪽에서 오른쪽으로 진행되며, 계층 구조에서 중복되는 클래스는 한 번만 확인
        - `class D(B, C) :` 의 경우 속성이 D에서 발견되지 않으면 B에서 찾고, 거기도 없으면, C에서 찾는다

### 4. super( ) 메서드

: 메서드 해석 순서(MRO)에 따라, 현재 클래스의 부모(상위) 클래스의 메서드나 속성에 접근할 수 있게 해주는 내장 함수

- super( )를 사용하면 직접 부모 클래스 이름을 적지 않아도, MRO에 따라 자동으로 올바른 메서드를 찾아 실행할 수 있다
- 다중 상속에서 super( )를 호출하면 상속 순서에 맞춰 여러 부모 클래스의 메서드를 순차적으로 실행할 수 있다
- 생성자나 오버라이딩된 메서드에서, super( )를 호출하면 부모 클래스의 초기화나 로직을 그대로 활용 가능하다
- 2가지 사용 사례
    1. 단일 상속 구조
        - 명시적으로 부모 클래스 이름을 적지 않아도 부모 메서드를 안전하게 호출할 수 있음
        - 나중에 부모 클래스 이름이 바뀌거나 상속 구조가 변경되어도 super( ) 호출 부분을 그대로 사용할 수 있어 유지보수성이 향상
        
        ```python
        # super를 사용하지 않았을 때
        class Person:
            def __init__(self, name, age, number, email):
                self.name = name
                self.age = age
                self.number = number
                self.email = email
        
        class Student(Person):
            def __init__(self, name, age, number, email, student_id):
                self.name = name
                self.age = age
                self.number = number
                self.email = email
                self.student_id = student_id
        
        # super를 사용했을 때
        class Person:
            def __init__(self, name, age, number, email):
                self.name = name
                self.age = age
                self.number = number
                self.email = email
        
        class Student(Person):
            def __init__(self, name, age, number, email, student_id):
                # super()를 통해 Person의 __init__ 메서드 호출
                super().__init__(name, age, number, email)
                self.student_id = student_id
        ```
        
    2. 다중 상속 구조
        - MRO 에 따라 각 클래스의 메서드를 찾아가기 때문에, 단순히 직계 부모만이 아니라 다중 상속 관계에서도 적절한 상위 클래스의 메서드를 안전하게 호출할 수 있음
        - `mro()` `__mro__` 를 사용해서 어떤 순서로 클래스를 찾아가는 지 확인하면서 코딩
        
        ```python
        # 다중 상속1
        class ParentA:
            def __init__(self):
                self.value_a = 'ParentA'  # 인스턴스 변수 value_a 를 갖는다
        
            def show_value(self):
                print(f'Value from ParentA: {self.value_a}')
        
        class ParentB:
            def __init__(self):
                self.value_b = 'ParentB'   # 인스턴스 변수 value_b 를 갖는다
        
            def show_value(self):
                print(f'Value from ParentB: {self.value_b}')
        
        class Child(ParentA, ParentB):
            def __init__(self):
                super().__init__()  # ParentA 클래스의 __init__ 메서드 호출 -> value_a 를 갖는다
                self.value_c = 'Child' # 인스턴스 변수 value_c를 갖는다
        
            def show_value(self):
                super().show_value()  # ParentA 클래스의 show_value 메서드 호출
                print(f'Value from Child: {self.value_c}')
        
        child = Child()   # Child 인스턴스 생성
        child.show_value()  # Child의 show_value 메서드 실행 -> 그 안에 ParentA 클래스의 메서드도 있으므로 같이 실행
        """
        Value from ParentA: ParentA
        Value from Child: Child
        """
        
        print(child.value_c)  # Child
        print(child.value_a)  # ParentA
        print(child.value_b)  # AttributeError: 'Child' object has no attribute 'value_b' 
           #-> value_b 는 인스턴스 변수에 없고 찾아갈 수도 없음!
        
        ```
        
        - Child 클래스가 ParentA, ParentB 를 모두 상속받고 있지만 ParentB 의 인스턴스 변수는 상속받지 못하고 있음
            
            → ParentA 에 `super().**init**()` 을 추가하면 MRO에 따라 Child 클래스가 `Child → ParentA → ParentB` 까지 init 함 → ParentB의 value_b도 출력할 수 있게 됨
            
        
        ```python
        # 다중 상속2
        class ParentA:
            def __init__(self):
                super().__init__()  # 얘를 추가
                self.value_a = 'ParentA'  # 인스턴스 변수 value_a 를 갖는다
        
            def show_value(self):
                print(f'Value from ParentA: {self.value_a}')
        
        class ParentB:
            def __init__(self):
                self.value_b = 'ParentB'   # 인스턴스 변수 value_b 를 갖는다
        
            def show_value(self):
                print(f'Value from ParentB: {self.value_b}')
        
        class Child(ParentA, ParentB):
            def __init__(self):
                super().__init__()  # ParentA 클래스의 __init__ 메서드 호출 -> value_a 를 갖는다
                self.value_c = 'Child' # 인스턴스 변수 value_c를 갖는다
        
            def show_value(self):
                super().show_value()  # ParentA 클래스의 show_value 메서드 호출
                print(f'Value from Child: {self.value_c}')
        
        child = Child()   # Child 인스턴스 생성
        child.show_value()  # Child의 show_value 메서드 실행 -> 그 안에 ParentA 클래스의 메서드도 있으므로 같이 실행
        """
        Value from ParentA: ParentA
        Value from Child: Child
        """
        
        print(child.value_c)  # Child
        print(child.value_a)  # ParentA
        print(child.value_b)  # ParentB
        ```
        
        - 즉 MRO 는 단순히 “직계 부모 클래스를 가리킨다” 가 아니라, MRO 순서를 기반으로 “현재 클래스의 다음 순서” 클래스(또는 메서드)를 가리킴
        
        ```python
        """
        1.1 Child 클래스의 인스턴스를 생성할 때 일어나는 일
            1.	child = Child() 호출 시, Child.__init__()가 실행
            2.	Child.__init__() 내부에서 super().__init__()를 호출
                - 여기서 Child의 super()는 MRO에 의해 ParentA의 __init__()를 가리킴
            3.	ParentA.__init__()로 진입
        
        1.2. ParentA.__init__() 내부
            1.	ParentA.__init__()에는 다시 super().__init__()가 있음
            2.	ParentA를 기준으로 MRO에서 “다음 클래스”는 ParentB, 따라서 ParentA의 super().__init__()는 ParentB.__init__() 호출
            3.	ParentB.__init__()가 실행되면서 self.value_b = 'ParentB'가 설정됨
            4.	ParentB.__init__()가 종료된 후, 다시 ParentA.__init__()로 돌아와 self.value_a = 'ParentA'가 설정됨
            5.	ParentA.__init__() 종료 후, 다시 Child.__init__()로 돌아감
            6.	마지막으로 Child.__init__() 내에서 self.value_c = 'Child'가 설정되고 종료
        
        1.3 결과적으로 child 인스턴스는 value_a, value_b, value_c 세 속성을 모두 갖게 됨
            - child.value_a → 'ParentA'
            - child.value_b → 'ParentB' 
            - child.value_c → 'Child'
        """
        ```
        
        <aside>
        💡
        
        MRO가 필요한 이유
        
        - 부모 클래스들이 여러 번 액세스 되지 않도록,
            
            각 클래스에서 지정된 왼쪽에서 오른쪽으로 가는 순서를 보존하고,
            
            각 부모를 오직 한 번만 호출하고,
            
            부모들의 우선순위에 영향을 주지 않으면서 서브 클래스를 만드는 단조적인 구조 형성
            
        
        → 신뢰성 있고 확장성 있는 클래스를 설계할 수 있다
        
        → 호출 순서가 예측 가능하게 유지되어, 코드의 재사용성과 유지보수성이 향상된다
        
        </aside>
        



### 클래스의 의미와 활용

알고리즘 문제 푸는데는 크게 도움이 되지 않을 수 있지만 실제 큰 프로그램을 설계하고 만들 때는 꼭 필요하다




## 활동 정리

| 개념 | 설명 |
| --- | --- |
| 상속(Inheritance) | 부모 클래스의 속성과 메서드를 자식 클래스가 물려받는 기능 |
| 오버라이딩(Overriding) | 부모 클래스의 메서드를 자식 클래스에서 같은 이름으로 재정의
(매개변수는 동일하게) |
| super( ) | 부모 클래스의 메서드를 호출할 때 사용하는 내장 함수 |
| 다중 상속 | 둘 이상의 클래스를 동시에 상속받는 구조 |
| MRO (Method Resolution Order) | 다중 상속 시 메서드를 탐색하는 우선 순서 |
| 예외 처리 (try-except) | 프로그램 실행 중 발생하는 예외를 처리하는 구조 |
| else - finally | try에서 예외가 없으면 else가 실행되고, finally는 항상 실행 |## 활동 정리

| 개념 | 설명 |
| --- | --- |
| 클래스(class) | 객체를 생성하기 위한 설계도 |
| 인스턴스(instance) | 클래스로부터 만들어진 실제 객체 |
| 인스턴스 변수 | 인스턴스마다 따로 가지는 변수 |
| 클래스 변수 | 모든 인스턴스가 공유하는 변수 |
| 인스턴스 메서드 | 인스턴스에서 호출되며 self 를 첫 인자로 받는 메서드 |
| 클래스 메서드 | 클래스에서 호출되며 cls를 첫 인자로 받는 메서드 |
| 스태틱 메서드 | 인스턴스나 클래스 정보 없이 독립적으로 동작하는 메서드 |
| 이름 공간 (namespace) | 변수들이 저장되는 공간, 인스턴스와 클래스는 서로 다른 이름 공간을 가짐 |
| 매직 메서드 | `__init__` `__str__` 처럼 특별한 이름을 가지며 자동으로 호출되는 메서드 |
| 데코레이터 | 함수나 메서드를 꾸며주는 특수한 함수 |