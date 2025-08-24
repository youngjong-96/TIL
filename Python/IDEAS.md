# 문제 해결 개념

## 최댓값 구하기
```python
max_val = 0
if compare_val > max_val:
    max_val = compare_val
```

## 자리 바꾸기

`A, B = B, A`

## 중첩 반복문 활용 - 안쪽 반복문 시작 숫자 늘리기
```python
for i in range(3):
    
    print(f"바깥쪽 루프 #{i+1} (i = {i})")
    # 안쪽 루프는 i 값에서 시작하여 i+3 직전까지 3번 반복합니다.
    # i=0 일 때: range(0, 3) -> 0, 1, 2
    # i=1 일 때: range(1, 4) -> 1, 2, 3
    # i=2 일 때: range(2, 5) -> 2, 3, 4
    for j in range(i, i + 3):
        print(f"  -> 안쪽 값: {j}")
    
    print("-" * 20) # 구분을 위한 라인
```
결과
```
바깥쪽 루프 #1 (i = 0)
  -> 안쪽 값: 0
  -> 안쪽 값: 1
  -> 안쪽 값: 2
--------------------
바깥쪽 루프 #2 (i = 1)
  -> 안쪽 값: 1
  -> 안쪽 값: 2
  -> 안쪽 값: 3
--------------------
바깥쪽 루프 #3 (i = 2)
  -> 안쪽 값: 2
  -> 안쪽 값: 3
  -> 안쪽 값: 4
--------------------
```

## 빈 배열의 인덱스를 사용하기 위해 배열값이 없는 리스트 생성하기

`list = [None] * x` : x개 원소 생성, None 대신 0을 넣을 때도 있음


## join 함수로 리스트 안에 있는 숫자 이어서 출력하기

```python
sample = [1, 2, 3, 4, 5]
print(",".join(map(str, sample)))
```
join 은 "문자열" 만 연결해주기 때문에 map 함수로 str 형으로 변환 후 연결한다


## 비트 연산자를 이용한 부분집합 만들기


```python
# 비트 연산자를 이용한 부분 집합 만들기
arr = [1,2,4]

n = len(arr)

for i in range(1 << n):  # 1 << n : 부분 집합의 개수
                         # 십진수 0~부분집합의 개수 까지를 2진수로 가지면 "bit배열이 만들어진다!"
    for j in range(n):   # 원소의 수만큼 비트를 비교하기 위해 반복하기 위한 for 문
        if i & (1 << j): # i 의 j번 비트가 1인지 확인
            print(arr[j], end=", ")  # j번 원소 출력
    print()
print()
```


## 회문 확인 - 길이의 절반만큼만 비교하면 된다

```python
def is_palindrome(txt):
	for i in range(len(txt)//2):  # 길이의 절반만큼만 비교하면 됨
		if txt[i] != txt[len(txt)-1-i]:   # 맨 앞 글자와 맨 뒤 글자가 같은지 비교
			return False
	return True

print(is_palindrome("level"))
print(is_palindrome("algorithm"))

>>>
True
False
```