# 파이썬의 필수 내장 함수, isinstance()

`isinstance()`는 특정 객체가 주어진 클래스 또는 자료형의 인스턴스인지 확인하는 함수

쉽게 말해, 객체의 종류(타입)를 검사하는 것

검사 결과가 맞으면 `True`, 아니면 `False`를 반환

```
만약 특정 문자열이 '문자'인지 혹은 '숫자'인지를 확인하려고 한것이라면
isalpha() 함수와 isdigit() 함수를 사용해야 함!
```
[isalpha_isdigit](Python/isalpha_isdigit.md)

## 사용법

`isinstance()` 함수의 기본 구조는 다음과 같습니다.

> ```python
> isinstance(object, classinfo)
> ```

-   `object`: 타입을 확인하고 싶은 객체입니다.
-   `classinfo`: 확인하려는 클래스 또는 자료형입니다. 여러 타입을 한 번에 확인하고 싶다면 **튜플** 형태로 묶어서 전달할 수 있습니다.

**classinfo 에 들어갈 수 있는 자료형**
- 기본 자료형: int, float, str, list, dict, set 등
- 사용자 정의 클래스: 사용자가 class 키워드로 직접 만든 클래스


### 기본 자료형 확인

변수가 특정 숫자, 문자열, 리스트 등의 기본 자료형에 속하는지 간단하게 확인할 수 있습니다.

```python
# 숫자 확인
number = 100
print(f"100은 정수인가? {isinstance(number, int)}")
# 출력: 100은 정수인가? True
print(f"100은 실수인가? {isinstance(number, float)}")
# 출력: 100은 실수인가? False

# 문자열 확인
text = "hello"
print(f"'hello'는 문자열인가? {isinstance(text, str)}")
# 출력: 'hello'는 문자열인가? True

# 여러 타입 중 하나인지 확인 (튜플 활용)
print(f"100은 정수 또는 실수인가? {isinstance(number, (int, float))}")
# 출력: 100은 정수 또는 실수인가? True
```

## `type()`과의 차이점: 상속 관계의 이해

`isinstance()`가 `type()` 함수보다 권장되는 가장 큰 이유는 **상속 관계**를 고려하기 때문입니다.

-   `type()`: 정확히 해당 클래스의 인스턴스인지만 확인합니다.
-   `isinstance()`: 부모 클래스의 인스턴스까지 `True`로 인식합니다.

예를 들어, `Animal`이라는 부모 클래스와 이를 상속받는 `Dog` 자식 클래스가 있다고 가정해 봅시다.

```python
# 부모 클래스
class Animal:
    pass

# 자식 클래스
class Dog(Animal):
    pass

# Dog 클래스의 인스턴스 생성
my_dog = Dog()
```

이때 type()과 isinstance()는 다음과 같이 다르게 동작합니다.

```Python
# 1. type() 사용
print(f"type()으로 Dog 확인: {type(my_dog) == Dog}")
# 출력: type()으로 Dog 확인: True
print(f"type()으로 Animal 확인: {type(my_dog) == Animal}")
# 출력: type()으로 Animal 확인: False (정확히 Animal 타입은 아니므로)

# 2. isinstance() 사용
print(f"isinstance()로 Dog 확인: {isinstance(my_dog, Dog)}")
# 출력: isinstance()로 Dog 확인: True
print(f"isinstance()로 Animal 확인: {isinstance(my_dog, Animal)}")
# 출력: isinstance()로 Animal 확인: True (상속 관계를 고려하므로)
```

my_dog은 Dog 클래스의 인스턴스이면서, 동시에 Dog이 Animal을 상속했기 때문에 Animal 클래스의 인스턴스이기도 합니다.

isinstance()는 이러한 상속 관계를 파악하여 '개는 동물이다'라는 논리적 관계를 True로 올바르게 반환합니다.

이처럼 유연하고 객체 지향적인 코드 작성이 필요할 때 isinstance()는 매우 유용합니다.

타입 체크가 필요하다면 type()보다는 isinstance()를 우선적으로 고려해 보세요!