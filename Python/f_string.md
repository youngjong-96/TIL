# f-string

참고: [https://soypablo.tistory.com/entry/대한민국에서-가장-자세한-f-string-가이드](https://soypablo.tistory.com/entry/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%97%90%EC%84%9C-%EA%B0%80%EC%9E%A5-%EC%9E%90%EC%84%B8%ED%95%9C-f-string-%EA%B0%80%EC%9D%B4%EB%93%9C)

### f-string은 “포맷 명세 미니 언어”를 지원한다!

포맷 명세 미니 언어: { } 안에 : 이후에 오는 기호들로 좀 더 다양한 형태의 데이터에 대한 출력을 자세히 제어

사용 시 장점

1. 유연성: 좀 더 유연하게 출력할 수 있다. ex. 소수점 자릿수, 날짜 및 시간 형식, 문자열 정렬, 공백 채우기
2. 가독성: 복잡한 문자열 구성을 간결하게 해준다 → 가독성 up! → 유지 보수 up!
3. 지역화: 숫자를 표시하는 방식이나, 날짜 형식을 지역에 따라 적절히 변경 가능
4. 디버깅:  = 연산자를 사용하여 표현식과 결과를 동시에 출력

```python
#소수점 표현
pi = 3.141592
print(f"Pi = {pi:.2f}")
>> Pi = 3.14

#숫자 쉼표로 구분
money = 10000000000
print(f"{money:,}")
>> 10,000,000,000
```

포맷 명세 미니 언어 요소들

- fill : 공백을 채울 문자를 지정
- align: 정렬 방식을 지정
    - 왼쪽 정렬: <
    - 오른쪽 정렬: >
    - 가운데 정렬: ^
- sign: 부호 표시를 지정
    - + : 양수와 음수 모두에 부호를 붙임
    - - : 음수에만 부호를 붙임
    - , : 양수에는 공백을, 음수에는 -를 붙임
- width: 출력할 데이터의 폭을 지정
- precision: 숫자형에 한해서, 소수점 이하 자리수 표현 설정

```python
# fill 과 width를 사용하는 예제
name = 'David'
print(f"{name:*^10}")
>> **David***

print(f"{name:!<10}")
>> David!!!!!

print(f"{name:^^10}")
>> ^^David^^^
```

<aside>
💡

: 포맷 명세 미니 언어에 변수를 사용하고 싶다면?!?!

</aside>

### 포맷 명세 미니 언어를 { }로 감싸면 됨ㅋㅋㅋㅋ

```python
word = "Test"
a = "^"
b = 10
c = '*'
print(f'{word:{c+a+str(b)}}')

>> ***Test***
```

단 숫자형은 str( )로 문자형으로 감싸주고 전체적으로 + 로 연결해줘야 함

디버깅에 유용한 = 지정자

f”{expr=}” 형태로 f-string을 작성하면, 해당 식의 텍스트, 등호, 평가된 표현식이 확장되어 출력

```python
word = "Hello world!"
print(f'{word=}')
>>word='Hello world!'
```