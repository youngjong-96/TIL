### 1. 순차 검색

- 검색 과정
    1. 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 찾는다
    2. 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환한다
    3. 자료구조의 마지막에 이를 때까지 검색 대상을 차지 못하면 검색 실패
- 검색 대상이 정렬 되어 있지 않은 경우
    - 찾고자 하는 원소의 순서에 따라 비교회수가 결정됨
    - 시간 복잡도 : O(n)
  
```python
# 
def sequential_search(a, n, key): # a = 배열, n = 찾는 횟수, key = 찾는 값
    i = 0
    while i < n and a[i] != key:
        i += 1
    if i < n : return i
    else: return -1


a = [1, 5, 3, 8, 10]
print(sequential_search(a, 10, 3))

>>> 
2
```

- 검색 대상이 정렬 되어 있지 않은 경우
    - 찾고자 하는 원소의 순서에 따라 비교회수가 결정됨
    - 시간 복잡도 : O(n)
    - 하지만! 실패할 경우에도 찾는 값보다 큰 값은 보지 않아서 효율이 좀 더 좋음


### 2. 이진 검색

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행
- 자료가 기본적으로 정렬된 상태여야 함!
- 검색 과정
    1. 자료의 중앙에 있는 원소를 고른다
    2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다
    3. 목표 값이 중앙 원소보다 작으면 왼쪽에서 다시 보고, 크면 오른쪽에서 본다
    4. 1~3을 반복한다
- 자료에 삽입이나 삭제가 발생했을 때 다시 정렬하는 작업이 필요하다

```python
# 이진검색 기본 코드
def binarysearch(a, n, key):  # a = 배열, n = 끝 값, key = 찾을 값
    start = 0
    end = n - 1
    while start <= end:
        middle = (start + end)//2
        if a[middle] == key:
            return middle
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return -1

a = [1, 2, 3, 4, 6, 7, 10, 12]
print(binarysearch(a, len(a), 2))

>> 
1
```