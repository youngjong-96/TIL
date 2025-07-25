# isalpha()와 isdigit()

💡 간단 요약
- `'문자열'.isalpha()`: 글자로만 이루어져 있나? (공백, 숫자, 특수문자 X)

- `'문자열'.isdigit()`: 숫자로만 이루어져 있나? (공백, 문자, 특수문자 X)

## isalpha(): 모든 문자가 '알파벳'인지 확인

`isalpha()` 함수는 문자열에 포함된 **모든 문자**가 **알파벳**일 때 `True`를, 그렇지 않으면 `False`를 반환합니다.

-   **알파벳의 범위**: 유니코드 상의 모든 문자(letter)를 포함합니다. 즉, 영어(a-z, A-Z)뿐만 아니라 **한글(ㄱ-힣)**, 일본어 등 다른 언어의 문자도 알파벳으로 취급합니다.
-   **주의**: 문자열에 **숫자, 공백, 특수문자**가 하나라도 포함되어 있으면 `False`를 반환합니다.

```python
# True를 반환하는 경우
print(f"'HelloWorld'.isalpha(): {'HelloWorld'.isalpha()}")
print(f"'한글'.isalpha(): {'한글'.isalpha()}")

# False를 반환하는 경우
print(f"'hello world'.isalpha(): {'hello world'.isalpha()}") # 공백 포함
print(f"'hello100'.isalpha(): {'hello100'.isalpha()}")   # 숫자 포함
print(f"'hello!'.isalpha(): {'hello!'.isalpha()}")     # 특수문자 포함
```

## isdigit(): 모든 문자가 '숫자'인지 확인

`isdigit()` 함수는 문자열에 포함된 **모든 문자**가 **숫자(0-9)**일 때 `True`를, 그렇지 않으면 `False`를 반환합니다.

-   **숫자의 범위**: 일반적으로 우리가 아는 아라비아 숫자(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)를 의미합니다.
-   **주의**: 문자열에 **알파벳, 공백, 특수문자(소수점, 음수 부호 포함)**가 하나라도 있으면 `False`를 반환합니다.

```python
# True를 반환하는 경우
print(f"'12345'.isdigit(): {'12345'.isdigit()}")

# False를 반환하는 경우
print(f"'123a'.isdigit(): {'123a'.isdigit()}")     # 알파벳 포함
print(f"'123 45'.isdigit(): {'123 45'.isdigit()}")   # 공백 포함
print(f"'12.34'.isdigit(): {'12.34'.isdigit()}")   # 소수점 포함
print(f"'-123'.isdigit(): {'-123'.isdigit()}")     # 음수 부호 포함
```