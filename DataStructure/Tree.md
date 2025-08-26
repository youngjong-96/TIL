### 그래프 입력받기

1. 인접행렬

```python
"""
6 5
1 4
1 3
2 3
2 5
4 6
"""
# 이런식으로 간선에 대한 정보를 입력받아 가지고 있다면,
lines = [list(map(int, input().split())) for _ in range(e)]

# 인접 행렬
    # 2차원 배열을 만들고 arr[i][j]가 True 라면 i -> j 로 통하는 길이 있음을 나타내도록 값을 채운다
    # 1. 일단 전체 배열을 만든다. (n개의 점이 있다면 최소 n*n의 2차원 배열이 필요)
    adj_mat = [[0] * (n+1) for _ in range(n+1)]
    # 2. 각 간선을 살펴보면서, adj_mat을 채운다.
    for line in lines:
        # line[0]에서 line[1]까지는 길이 존재함을 의미하므로
        adj_mat[line[0]][line[1]] = 1
        # 양방향이라면
        # line[1]에서 line[0]까지 길도 존재한다
        adj_mat[line[1]][line[0]] = 1
        
        
>>>
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 1, 0, 0]
[0, 0, 0, 1, 0, 1, 0]
[0, 1, 1, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0, 1]
[0, 0, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0]

```

1. 인접 리스트
- 리스트의 인덱스를 노드 번호라고 생각하고 해당 부분에 인접한 노드들을 기록한다

```python
"""
6 5
1 4
1 3
2 3
2 5
4 6
"""
# 이런식으로 간선에 대한 정보를 입력받아 가지고 있다면,
lines = [list(map(int, input().split())) for _ in range(e)]

# 인접 리스트
    # 2차원 배열을 만들고,
    # arr[i]에 리스트(또는 다른 자료형)을 할당한 다음
    # i에 저장된 리스트에 연결된 정점들을 넣어준다
    adj_lst = [[] for _ in range(n+1)]

    # 각 간선을 살펴보면서, adj_lst를 갱신한다
    for line in lines:
        # line[0]에서 line[1]이 도달 가능함을 의미함으로
        adj_lst[line[0]].append(line[1])
        # 양방향의 경우에는
        adj_lst[line[1]].append(line[0])

    for row in adj_lst:
        print(row)
        
        
>>>
[]
[4, 3]
[3, 5]
[1, 2]
[1, 6]
[2]
[4]
```