## 에러와 예외

### 1. 디버깅

: 소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정

- 디버깅 방법
    - print 함수 활용
    - 개발환경(text editor, IDE) 등에서 제공하는 기능 활용
    - Python tutor 활용 (단순 파이썬 코드인 경우)
    - 뇌 컴파일, 눈 디버깅 …?!

### 2. 에러

: 프로그램 실행 중에 발생하는 예외 상황

- 에러 유형
    - 문법 에러(Syntax Error) - 구문이 안 맞음
        - Invalid syntax (문법 오류)
        - assign to literal (잘못된 할당)
        - Unterminated string literal
    - 예외(Exception) - 프로그램 실행 중 감지되는 에러

### 3. 예외

- 내장 예외 : 예외 상황을 나타내는 예외 클래스들
    - 내장 예외는 파이썬에서 이미 정의되어 있으며, 특정 예외 상항에 대한 처리를 위해 사용
    - ZeroDivisionError : 0으로 나눌 때
    - NameError : 이름 못찾음
    - TypeError : 타입 불일치, 인자 누락, 인자 초과, 인자 타입 불일치
    - ValueError : 부적절한 값을 가진 인자를 받았고 구체적인 예외로 설명되지 않는 경우
    - IndexError : 시퀀스 인덱스가 범위 벗어남
    - KeyError : 딕셔너리에 키 없음
    - ImportError : import 하려는 이름을 찾을 수 없음
    - ModuleNotFoundError : 모듈을 찾을 수 없을 때
    - KeyboardInterrupt : 사용자가 Control-C 또는 Delete를 누를 때 발생
    - IndentationError : 잘못된 들여쓰기

## 예외 처리

- 예외처리 사용 구문
    - try : 예외가 발생할 수 있는 코드 작성
    - except : 예외가 발생했을 때 실행할 코드 작성
    - else : 예외가 발생하지 않았을 때 실행할 코드 작성
    - finally : 예외 발생 여부와 상관없이 항상 실행
    
    ```python
    # 예외처리 구조 미리보기
    try:
        x = int(input('숫자를 입력하세요: '))
        y = 10 / x
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다.')
    except ValueError:
        print('유효한 숫자가 아닙니다.')
    else:
        print(f'결과: {y}')
    finally:
        print('프로그램이 종료되었습니다.')
    ```
    

### 1. try & except

```python
# try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')

try:
    num = int(input('숫자입력 : '))
except ValueError:
    print('숫자가 아닙니다.')
    
>>>
0으로 나눌 수 없습니다.
숫자입력 : a
숫자가 아닙니다.
```

### 2. 복수 예외 처리

```python
# 복수 예외처리 예시 1
try:
    num = int(input('100을 나눌 값을 입력하시오 : '))
    print(100 / num)
except (ValueError, ZeroDivisionError):
    print('제대로 입력해주세요.')

# 복수 예외처리 예시 2
try:
    num = int(input('100을 나눌 값을 입력하시오 : '))
    print(100 / num)
except ValueError:
    print('숫자를 넣어주세요.')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('에러가 발생했습니다.')
```

### 3. else & finally

```python
# else & finally 예시

try:
    x = int(input('숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:     # 0으로 나눌 시
    print('0으로 나눌 수 없습니다.')
except ValueError:            # 숫자가 아닌 다른 값을 입력했을 시
    print('유효한 숫자가 아닙니다.')
else:                         # 오류가 발생하지 않으면
    print(f'결과: {y}')
finally:                      # 오류 발생 여부와 상관없이 실행
    print('프로그램이 종료되었습니다.')
```

## 참고

### 1. 예외 처리 주의사항

![image.png](image.png)

공식 문서 참고 : [https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy](https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy)

- 내장 예외 클래스는 위와 같은 상속구조를 가지기 때문에 except 절로 분기 시 하위 클래스를 먼저 확인 할 수 있도록 작성해야 한다

```python
# 잘못된 예시

try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
except Exception:
    print('숫자를 넣어주세요.')
# ZeroDivisionError는 Exception의 하위 클래스이므로 Exception보다 먼저 작성해야 함
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('에러가 발생하였습니다.')
    

# 잘못된 예시를 수정(옳은 코드)

try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
# 1) 구체적인 예외부터
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('숫자를 넣어주세요.')
# 2) 마지막에 광범위한 예외(Exception)
except Exception:
    print('에러가 발생하였습니다.')
```

### 2. 예외 객체 다루기

- as 키워드로 다루기

```python
# as 키워드 예시
my_list = []

try:
    number = my_list[1]
except IndexError as error:
    # list index out of range가 발생했습니다.
    print(f'{error}가 발생했습니다.')
```

- if-else 추가하기

```python
# try-except 안에서 if-else 사용 예시
try:
    x = int(input('숫자를 입력하세요: '))
    if x < 0:
        print('음수는 허용되지 않습니다.')
    else:
        print('입력한 숫자: ', x)
except ValueError:
    print('오류 발생')
```

### 3. EAFP & LBYL

- EAFP (Easier to Ask for Forgiveness than Permission) - 예외처리를 중심으로 하는 접근방식
- LBYL (Look Before You Leap) - 값 검사를 중심으로 하는 접근 방식

| EAFP | LBYL |
| --- | --- |
| “일단 실행하고 예외를 처리” | “실행하기 전에 조건을 검사” |
| 코드를 실행하고 예외가 발생하면 예외처리를 수행 | 코드 실행 전에 조건문 등을 사용하여 예외 상황을 미리 검사하고, 예외 상황을 피하는 방식 |
| 코드에서 예외가 발생할 수 있는 부분을 미리 예측하여 대비하는 것이 아니라, 예외가 발생한 후에 예외를 처리 | 코드가 좀 더 예측 가능한 동작을 하지만, 코드가 더 길고 복잡해질 수 있음 |
| 예외 상황을 예측하기 어려운 경우에 유용 | 예외 상황을 미리 방지하고 싶을 때 유용 |