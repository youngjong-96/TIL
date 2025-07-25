# 문제 해결 개념

## 최댓값 구하기
```
max_val = 0
if compare_val > max_val:
    max_val = compare_val
```

## 자리 바꾸기

`A, B = B, A`

## 중첩 반복문 활용 - 안쪽 반복문 시작 숫자 늘리기
```
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

`list = [None] * x` : x개 원소 생성







