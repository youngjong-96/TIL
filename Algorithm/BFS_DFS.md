# DFS - 깊이우선탐색



# BFS - 너비우선탐색

- 탐색 시작점의 인접한 정점들을 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
- BFS 기본형
    - `visited` : 해당 노드가 처리되었음(방문했음)을 기록하기 위한 리스트
    - `queue` : 방문할 노드들을 저장할 큐
    - 초기화
        1. visited 배열 만들기
        2. queue 생성
        3. queue에 시작점 enqueue
    - while 문
        1. queue의 첫 번째 원소 반환
        2. 방문하지 않은 곳이라면 방문한 것으로 표시
        3. 연결된 접점들을 확인하면서 방문하지 않은 노드들을 추가

```python
def bfs(graph, start):   # 그래프, 시작점
    visited = [0]*(n+1)  # visited 리스트 만들기, n = 정점의 개수
                         #(2차배열을 인자로 받은 경우 2차배열 visited 생성) 

    queue = []   # 큐 생성

    queue.append(start)  # 시작점을 큐에 삽입

    while queue:   # 큐에 뭔가 남아있는 동안
        t = queue.pop(0)   # 큐의 첫번째 원소 반환
        if not visited[t]:   # 방문하지 않은 곳이라면
            visited[t] = True   # 방문한 것으로 표시하고
            visit(t)         # 정점 t 에서 할 일

            for i in graph[t]:  # t와 연결된 모든 정점에 대해
                if not visited[i]:    # 방문되지 않은 곳이라면
                    queue.append(i)   # 큐에 넣기(다음에 탐색할 수 있도록)
```

- BFS 유형 2
    - `visited` 배열에 출발점으로부터의 거리를 기록

```python
def bfs(graph, start, n):   # 그래프, 시작점
    visited = [0]*(n+1)  # visited 리스트 만들기 (2차배열을 인자로 받은 경우 2차배열 visited 생성) n = 정점의 개수

    queue = []   # 큐 생성

    queue.append(start)  # 시작점을 큐에 삽입
    visited[start] = 1   # 시작점을 방문했음 표시
    
    while queue:   # 큐에 뭔가 남아있는 동안
        t = queue.pop(0)   # 큐의 첫번째 원소 반환
            visit(t)         # 정점 t 에서 할 일

            for i in graph[t]:  # t와 연결된 모든 정점에 대해
                if not visited[i]:    # 인큐되지 않은 곳이라면
                    queue.append(i)   # 큐에 넣기(다음에 탐색할 수 있도록)
                    visited[i] = visited[t] + 1    # n으로 부터 1만큼 이동 (시작점으로부터 거리를 측정)
```

- BFS 유형 3
    - 1번 부터 모든 정점을 너비우선탐색하여 경로를 출력

```python
"""
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
"""

def bfs(start, V):
    # 초기화
    visited = [0] * (V+1)   # visited 배열 생성
    q = [start]             # queue 초기화
    visited[start] = 1      # visited 방문 표시

    # 반복
    while q:
        t = q.pop(0)        # 처음값 가져오기
        print(t, end=", ")  # 노드 t에서 할 일
        for i in adj_lst[t]:  # 인접한 노드들 가져오기
            if visited[i] == 0:   # 방문한 적이 없다면
                q.append(i)       # queue에 추가한다
                visited[i] = visited[t] + 1   # visited에 거리를 추가

# 노드 수, 간선 수
V, E = map(int, input().split())

# 간선 정보
arr = list(map(int, input().split()))

# 인접리스트
adj_lst = [[] for _ in range(V+1)]  # V 번행까지 비어있는 리스트 준비
# 2개씩 가져와서 인접리스트에 저장
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_lst[v1].append(v2)
    adj_lst[v2].append(v1)

bfs(1, V)

>>>
1, 2, 3, 4, 5, 7, 6, 
```

