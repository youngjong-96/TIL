## 조건문

: 주어진 조건식을 평가하여 해당 조건이 참이면 실행

```python
## if문 기본구조

if 조건1:
    조건1을 만족할 때 실행할 코드
elif 조건2:
    조건2를 만족할 때 실행할 코드
elif 조건3:
    조건3을 만족할 때 실행할 코드
else:
    모든 조건을 만족하지 않으면 실행할 코드
```

## 반복문

: 주어진 코드 블록을 여러 번 반복해서 실행하는 구문

- for 문: iterable 객체 요소들을 반복 / 반복 횟수가 정해져 있음
    1. 문자열 순회
        
        ```python
        country = 'Korea'
        
        for char in country:
            print(char)
            
        >>
        K
        o
        r
        e
        a
        ```
        
    2. range 순회
        
        ```python
        for i in range(5):
            print(i)
            
        >>
        0
        1
        2
        3
        4
        ```
        
    3. 딕셔너리 순회
        
        ```python
        my_dict = {
            'x': 10,
            'y': 20,
            'z': 30,
        }
        
        for key in my_dict:
            print(key)          # 딕셔너리 기본적으로는 key가 출력
            print(my_dict[key]) # 값 출력하려면 이렇게
            
        >>>
        x
        10
        y
        20
        z
        30
        ```
        
    4. 인덱스로 리스트 순회
        
        ```python
        # 인덱스를 이용해서 기존 리스트에 요소들에 2를 곱한 후 다시 할당하는 코드
        
        numbers = [4, 6, 10, -8, 5]
        
        for i in range(len(numbers)):
            numbers[i] = numbers[i] * 2
        
        print(numbers)
        
        >>>
        [8, 12, 20, -16, 10]
        ```
        
    5. 중첩 반복문
        
        ```python
        outers = ['A', 'B']
        inners = ['c', 'd']
        
        for outer in outers:
            for inner in inners:
                print(outer, inner)
                
         >>>
         A, c
         A, d
         B, c
         B, d
        ```
        
    6. 중첩 리스트 순회
        
        ```python
        # 중첩 리스트 순회
        elements = [['A', 'B'], ['c', 'd']]
        
        # 1
        for elem in elements:
            print(elem)
        
        >>>
        ['A', 'B']
        ['c', 'd']
        
        # 2
        for elem in elements:
            for item in elem:
                print(item)
             
        >>>
        A
        B
        c
        d
        ```
        
    
    <aside>
    💡
    
    IM 수료 위해서는 2차원 리스트를 잘 다루는게 중요 !!!!
    
    위에서 2번 예시, 즉 안쪽 요소들을 출력하는게 중요
    
    </aside>
    
- while 문 : **조건**이 참인 동안 반복 / 반복 횟수가 정해지지 않은 경우 사용
    
    <aside>
    💡
    
    while 문은 **조건**을 꼭 잘 생각하기
    
    반대로 생각하기 쉬워서 다른 제어문과 같이 사용할 때 한 번 더 생각해봐야 함
    
    조건에 사용할 변수는 while 문 밖에
    
    </aside>
    

- 반복 제어 키워드
    - break : 남은 코드를 무시하고 가까운 반복을 빠져나감
    - continue : 다음 코드는 무시하고 가까운 다음 반복을 수행
    - pass : ‘아무 동작도 하지 않음’을 명시적으로 나타내는 키워드, 틀을 유지하기 위한 구조적인 키워드

## 유용한 내장 함수 map & zip

- map 함수 : map(function, iterable)
    
    : 반복 가능한 데이터구조의 모든 요소에 function을 적용하고, 그 결과 값을 map **객체**로 반환
    
    → 객체로 반환하므로 출력해서 보려면 for 문이나 list( ) 함수를 사용해야 함
    
    → 객체로 반환하는 건 메모리 효율성 때문
    
- zip 함수 : zip(iterable, iterable, …)
    
    : 여러 개의 반복 가능한 데이터 구조를 묶어서 같은 위치에 있는 값들을 하나의 tuple로 만들고 zip 객체로 반환
    
    ```python
    # 개수가 안 맞으면 맞는 것만 함
    
    girls = ['jane', 'ashley']  # 요소 2개
    boys = ['peter']            # 요소 1개
    pair = zip(girls, boys)
    
    print(pair)  # <zip object at 0x000001C76DE58700>
    print(list(pair))  # [('jane', 'peter')]
    ```
    
    ```python
    # zip 함수 활용
    kr_scores = [10, 20, 30, 50]
    math_scores = [20, 40, 50, 70]
    en_scores = [40, 20, 30, 50]
    
    for student_scores in zip(kr_scores, math_scores, en_scores):
        print(student_scores)
        
    >>>
    (10, 20, 40)
    (20, 40, 20)
    (30, 50, 30)
    (50, 70, 50)
    ```
    
    ```python
    # zip 함수 활용 (전치 행렬)
    scores = [
        [10, 20, 30],
        [40, 50, 39],
        [20, 40, 50],
    ]
    
    for score in zip(*scores):
        print(score)
       
    >>>
    (10, 40, 20)
    (20, 50, 40)
    (30, 39, 50)
    ```
    

<aside>
💡

내장 함수 help를 사용해 모듈에 무엇이 들어있는지 확인할 수 있음!

`help(math)`

</aside>

## 참고

### for-else 문법

- if와 다르게 반복문이 정상적으로 모두 수행되었을 때, else 블록이 실행
- 검색, 검증 로직에서 활용
- while-else 문도 존재하며 동작 규칙은 동일
- break 키워드로 반복이 종료되면 else 문을 실행하지 않음

```python
# for-else 구문 기본
for i in range(5):
    print(i)
    if i == 3:
        # break 문이 실행되면 else 블록은 실행되지 않음
        print('반복이 중단되었습니다.')
        break
else:
    print('이 메시지는 출력되지 않습니다.')
```

```python
# for-else 구문 활용 - 중복 아이디 찾기

registered_ids = ['admin', 'user01', 'guest', 'user02']
id_to_check = 'guest'  # 이미 리스트에 존재하는 아이디

for existing_id in registered_ids:
    if existing_id == id_to_check:
        print('이미 사용 중인 아이디입니다.')
        break  # 중복 아이디를 찾았으므로 확인 절차를 중단
else:
    # for 루프가 break로 중단되었기에 이 부분은 실행되지 않음
    print('사용 가능한 아이디입니다.')
```

### enumerate 함수

`enumerate(iterable, start=0)`

: iterable 객체의 각 요소에 대해 인덱스와 값을 함께 반환하는 내장함수 → 번호를 붙여줌

```python
# enumerate 함수 활용 1
# start 인자를 사용하여 인덱스 번호를 1부터 출력
movies = ['인터스텔라', '기생충', '인사이드 아웃', '라라랜드']
for idx, title in enumerate(movies, start=1):
    print(f"{idx}위: {title}")
    
>>>
1위: 인터스텔라
2위: 기생충
3위: 인사이드 아웃
4위: 라라랜드
```

```python
# enumerate 함수 활용 2
# 인덱스 정보를 활용하여 특정 조건에 맞는 요소 찾기
respondents = ['은지', '정우', '소민', '태호']
answers = ['', '좋아요', '', '괜찮아요']

for i, response in enumerate(answers):
    if response == '':
        print(f"{respondents[i]} 미제출")
        
 >>>
은지 미제출
소민 미제출
```

## 핵심키워드

| 개념 | 설명 |  |
| --- | --- | --- |
| 모듈 Module) | 특정 기능들을 묶어놓은 파이썬 파일 |  |
| 패키지 (Package) | 여러 모듈들을 묶어놓은 디렉토리 |  |
| 제어문 | 코드의 실행 흐름을 제어하는 문법 | if, for, while |
| 반복문 | 특정 조건에 따라 코드 실행 여부를 결정 |  |
| break | 반복문을 즉시 종료 |  |
| continue | 반복문의 현재 실행을 건너뛰고 다음 반복으로 넘어감 |  |
| map( ) | 반복 가능한 객체의 모든 요소에 함수 적용 | list( map( str, [1, 2, 3] ) ) |
| zip( ) | 여러 반복 가능한 객체의 요소를 짝지어 반환 | list( zip( [1, 2], [’a’, ‘b’] ) ) |