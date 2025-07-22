`sorted()` 함수는 파이썬의 내장 함수로, 리스트나 튜플 같은 반복 가능한(iterable) 데이터를 정렬하여 새로운 리스트로 반환합니다. 원본 데이터는 그대로 유지됩니다.

## `sorted()` 함수의 기본 구조
함수의 기본 형태는 다음과 같습니다.


```python
sorted(iterable, *, key=None, reverse=False)
```
- `iterable`: 정렬할 데이터입니다. (예: 리스트, 튜플, 딕셔너리 등)

- `key` (선택 사항): 정렬의 기준을 정하는 함수입니다. 지정하지 않으면 요소 자체가 기준이 됩니다.

- `reverse` (선택 사항): 정렬 순서를 지정합니다.

    - `False` (기본값): 오름차순 (작은 값부터 큰 값 순서).

    - `True`: 내림차순 (큰 값부터 작은 값 순서).

## 기본 사용법
`key`나 `reverse` 인자 없이 사용하면 기본적으로 오름차순으로 정렬됩니다.

```python
# 숫자 리스트 정렬
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_numbers = sorted(numbers)
print(f"원본: {numbers}")
print(f"정렬 후: {sorted_numbers}")
# 원본: [3, 1, 4, 1, 5, 9, 2]
# 정렬 후: [1, 1, 2, 3, 4, 5, 9]

# 문자열 리스트 정렬 (알파벳 순)
fruits = ["banana", "apple", "cherry", "avocado"]
sorted_fruits = sorted(fruits)
print(f"정렬 후: {sorted_fruits}")
# 정렬 후: ['apple', 'avocado', 'banana', 'cherry']
```

## `reverse` 인자: 정렬 순서 바꾸기
`reverse=True`를 설정하면 내림차순으로 정렬할 수 있습니다.

```python
numbers = [3, 1, 4, 1, 5, 9, 2]
descending_numbers = sorted(numbers, reverse=True)
print(f"내림차순 정렬: {descending_numbers}")
# 내림차순 정렬: [9, 5, 4, 3, 2, 1, 1]
```

## `key` 인자: 정렬 기준 직접 정하기 ✨
`key`는 `sorted()` 함수의 핵심 기능으로, 복잡한 데이터를 원하는 기준으로 정렬할 수 있게 해줍니다.

1. 내장 함수를 `key`로 사용하기 (예: `len`)
문자열의 길이를 기준으로 정렬하고 싶을 때 `len` 함수를 `key`로 사용할 수 있습니다.

```Python

fruits = ["banana", "apple", "kiwi", "cherry"]
# 각 단어의 길이를 기준으로 오름차순 정렬
sorted_by_length = sorted(fruits, key=len)
print(f"길이 순 정렬: {sorted_by_length}")
# 길이 순 정렬: ['kiwi', 'apple', 'banana', 'cherry']
```

2. lambda 함수를 key로 사용하기
리스트 안에 튜플이나 딕셔너리가 있을 때 특정 요소를 기준으로 정렬할 수 있습니다.

```Python

# (학생, 점수) 튜플 리스트
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

# 점수(튜플의 1번 인덱스)를 기준으로 내림차순 정렬
sorted_by_score = sorted(students, key=lambda item: item[1], reverse=True)
print(f"점수 순 정렬: {sorted_by_score}")
# 점수 순 정렬: [('Bob', 92), ('Alice', 85), ('Charlie', 78)]
```

`lambda item: item[1]`은 리스트의 각 `item`(튜플)에 대해 `item[1]`(점수)을 반환하라는 의미의 간단한 함수입니다. `sorted()`는 이 반환된 점수를 기준으로 순서를 정합니다.

## sorted()와 .sort()의 차이점 💡
| 구분 | **`sorted()` 함수** | **`.sort()` 메서드** |
| --- | --- | --- |
| **반환값** | 정렬된 **새로운 리스트**를 반환 | 아무것도 반환하지 않음 (`None`) |
| **원본 데이터**| 원본을 **변경하지 않음** | 원본 리스트를 **직접 수정** (in-place) |
| **사용 대상** | **모든 반복 가능한 객체** (리스트, 튜플, 딕셔너리 등) | **리스트**에서만 사용 가능 |


`sorted()` 예시

```Python

my_list = [5, 2, 8]
new_list = sorted(my_list)

print(f"sorted() 결과: {new_list}") # sorted() 결과: [2, 5, 8]
print(f"원본 리스트: {my_list}") # 원본 리스트: [5, 2, 8]
```
`.sort()` 예시

```Python

my_list = [5, 2, 8]
result = my_list.sort()

print(f".sort() 결과: {result}") # .sort() 결과: None
print(f"원본 리스트: {my_list}") # 원본 리스트: [2, 5, 8]
```