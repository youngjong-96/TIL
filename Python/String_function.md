# 문자열 범위 선택

**파이썬은 인덱싱에서 -를 활용해 뒤에서부터 인덱싱을 지원한다**

문자열[start, end, skip]

```
word = 'Hello World!'
print(word[10: 5: -1])  #10번째 인덱스부터 6번째까지 역순으로 출력

>> dlroW
```

# 문자열 함수

### count(): 문자열 출현 횟수 확인

### len() : 문자열 길이 확인

### find(찾을 값 , 시작 위치) : 왼쪽에서부터 문자열 찾기
첫 번째 찾은 값의 인덱스 번호 반환
찾는 값이 없으면 '-1' 반환

### rfind() : 오른쪽에서부터 문자열 찾기
첫 번째 찾은 값의 인덱스 번호 반환
찾는 값이 없으면 '-1' 반환

### index() : 문자열 찾기
첫 번째 찾은 값의 인덱스 번호 반환
찾는 값이 없으면 value error 발생

### join() : 문자열의 삽입
사용법이 좀 직관적이지 않음(지극히 개인적)
concatanate 같은 느낌인데 중간중간 삽입임
```
word = '가나다라마바사'
print(', '.join(word))

>> 가, 나, 다, 라, 마, 바, 사
```

### capitalize() : 첫번째 문자만 대문자로 변경

### lower() : 모든 문자열을 소문자로 한 새로운 문자열 반환

### upper() : 모든 문자열을 대문자로 한 새로운 문자열 반환

### lstrip() : 왼쪽 공백 제거 

### rstrip() : 오른쪽 공백 제거
sys.stdin.readline()이 \n(개행문자)도 포함해서 읽어서 함께 사용하는 경우 있음

### strip() : 양쪽 공백 제거

### replace(찾을 문자열, 교체 문자열, 갯수) : 찾을 문자열과 교체 문자열을 인자로 사용해 교체
```
str = '10....20....30....40....50'
print(str.replace('.'*4, "\t"))

>>>10    20    30    40    50
```

### split() : 전달된 인자로 문자열을 잘라 이를 항목으로 갖는 리스트 생성
`word = map(int, inpu().split())`

### isdigit() : 숫자문자열인 경우 True 반환

---



## 문자열을 마스크 문자열로 치환하기

```
data_str = "파이썬은 클래스를 이용해 객체를 생성하는 객체지향 프로그래밍 언어입니다."
print(f"{data_str}")

mask_str = input("마스킹할 문자열을 입력하세요: ")

find_str = input("찾을 문자열을 입력하세요: ")

idx = -1
count = 1
while True:
    idx = data_str.find(find_str, idx +1)
    if idx != -1:
        print("[{0}] ~ [{1}]".format(idx, idx + len(find_str) - 1))
        new_str = data_str.replace(find_str, mask_str, count)
        print(new_str)
        count += 1
    else:
        break
print(idx)
```
