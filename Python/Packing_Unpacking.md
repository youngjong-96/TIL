# 파이썬 패킹(Packing)과 언패킹(Unpacking) 비교

네, 파이썬의 **패킹(Packing)**과 **언패킹(Unpacking)**은 서로 반대되는 개념으로, 함께 이해하면 코드를 훨씬 유연하고 간결하게 작성할 수 있습니다.

핵심적으로 **패킹은 여러 개의 값을 하나로 묶는 것**이고, **언패킹은 묶여 있는 하나의 값을 여러 개로 푸는 것**입니다.

---

### 1. 패킹 (Packing) 📦

**패킹**은 여러 개의 변수나 값들을 모아 하나의 튜플(tuple)이나 딕셔너리(dictionary) 같은 컬렉션으로 묶는 과정을 말합니다.

#### **예시 1: 변수 할당 시 자동 패킹**

여러 값을 쉼표로 구분하여 하나의 변수에 할당하면, 파이썬은 이 값들을 자동으로 튜플로 묶어줍니다.

```python
# 10, 'hello', True 세 개의 값을 packed_values 라는 하나의 튜플로 묶음 (패킹)
packed_values = 10, 'hello', True

print(packed_values)
# 출력: (10, 'hello', True)
print(type(packed_values))
# 출력: <class 'tuple'>
```

#### 예시 2: 함수 인자 패킹 (*args, kwargs)
함수를 정의할 때, 정해지지 않은 개수의 인자들을 받기 위해 사용합니다.

- *args: 여러 개의 **위치 인자(positional arguments)** 를 하나의 튜플로 묶습니다.

- \**kwargs: 여러 개의 **키워드 인자(keyword arguments)** 를 하나의 딕셔너리로 묶습니다.

```Python
def argument_packer(*args, **kwargs):
    print(f"위치 인자들 (args): {args}")      # 튜플로 패킹됨
    print(f"키워드 인자들 (kwargs): {kwargs}") # 딕셔너리로 패킹됨

# 함수 호출 시 전달된 여러 인자들이 args와 kwargs에 각각 패킹됨
argument_packer(1, 2, 'three', name='Alice', age=30)

# 출력:
# 위치 인자들 (args): (1, 2, 'three')
# 키워드 인자들 (kwargs): {'name': 'Alice', 'age': 30}
```

### 언패킹 (Unpacking) 🎁
**언패킹** 은 리스트, 튜플, 딕셔너리 등 컬렉션 안에 있는 요소들을 개별 변수들로 풀어 할당하는 과정을 말합니다.

#### 예시 1: 변수 할당 시 언패킹
컬렉션의 요소 개수와 할당받을 변수의 개수가 일치해야 합니다.

```Python

packed_tuple = (10, 'hello', True)

# packed_tuple 안의 요소들을 a, b, c 세 개의 변수로 풀어 할당 (언패킹)
a, b, c = packed_tuple

print(a) # 출력: 10
print(b) # 출력: 'hello'
print(c) # 출력: True
```

*를 사용하면 개수가 맞지 않아도 유연하게 언패킹할 수 있습니다. (확장 언패킹, Extended Unpacking)

```Python

numbers = [1, 2, 3, 4, 5]

# 첫 번째와 마지막 요소를 제외한 나머지를 middle 리스트로 언패킹
first, *middle, last = numbers

print(first)  # 출력: 1
print(middle) # 출력: [2, 3, 4]
print(last)   # 출력: 5
```

#### 예시 2: 함수 인자 언패킹
함수를 호출할 때, 리스트나 딕셔너리 앞에 * 또는 **를 붙여 그 안의 요소들을 인자로 풀어 전달합니다.

- *: 리스트나 튜플을 풀어서 위치 인자로 전달합니다.

- **: 딕셔너리를 풀어서 키워드 인자로 전달합니다.

```Python

def calculate(x, y, z):
    return x + y - z

my_list = [10, 20, 5]

# my_list를 언패킹하여 calculate(10, 20, 5)와 동일하게 호출
result = calculate(*my_list)
print(result) # 출력: 25

def show_user_info(name, age):
    print(f"이름: {name}, 나이: {age}")

user_data = {'name': 'Bob', 'age': 40}

# user_data 딕셔너리를 언패킹하여 show_user_info(name='Bob', age=40)와 동일하게 호출
show_user_info(**user_data)
# 출력: 이름: Bob, 나이: 40
```

### 한눈에 보는 비교 정리 ↔️

| 구분 (Category) | 패킹 (Packing) 📦 | 언패킹 (Unpacking) 🎁 |
| :--- | :--- | :--- |
| **개념** | 여러 개의 값을 **하나의 컬렉션으로 묶음** | 하나의 컬렉션 안의 값들을 **여러 변수로 품** |
| **방향** | `값1, 값2, ...` → `하나의 변수` | `하나의 컬렉션` → `변수1, 변수2, ...` |
| **주요 사용처** | 변수 할당, **함수 정의** (`*args`, `**kwargs`) | 변수 할당, **함수 호출** |
| **연산자 `*`** | 여러 위치 인자를 **하나의 튜플로 묶음** <br> `def func(*args):` | 리스트/튜플을 **여러 위치 인자로 품** <br> `func(*my_list)` |
| **연산자 `**`** | 여러 키워드 인자를 **하나의 딕셔너리로 묶음** <br> `def func(**kwargs):` | 딕셔너리를 **여러 키워드 인자로 품** <br> `func(**my_dict)` |