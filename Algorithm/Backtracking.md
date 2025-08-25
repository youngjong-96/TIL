# Backtracking 알고리즘

Backtracking은 해를 찾는 과정에서 **해가 될 가능성이 없는 경로를 더 이상 탐색하지 않고 뒤로 돌아와(backtrack) 다른 경로를 탐색**하는 알고리즘이에요. 쉽게 말해, 미로 찾기와 비슷하다고 생각할 수 있어요. 길을 가다가 막다른 골목에 다다르면 왔던 길로 되돌아가서 다른 갈림길로 가보는 것처럼요.

이 알고리즘은 보통 다음과 같은 문제를 해결하는 데 사용돼요.

* **결정 문제**: 해가 존재하는지 확인하는 문제 (예: 미로 탈출이 가능한가?)
* **최적화 문제**: 최적의 해를 찾는 문제 (예: 최단 경로)
* **열거 문제**: 모든 해를 찾는 문제 (예: 모든 가능한 순열 찾기)

---

## 1. Backtracking 작동 원리

백트래킹은 보통 재귀 함수로 구현되며, 다음과 같은 단계를 거쳐요.

1.  **상태 공간 트리(State Space Tree)**: 문제를 트리 형태로 모델링합니다. 트리의 각 노드는 문제의 부분적인 해를 나타내고, 리프 노드는 완전한 해나 해가 없는 상태를 나타냅니다.
2.  **깊이 우선 탐색(DFS)**: 트리의 한 경로를 따라 깊게 탐색합니다.
3.  **유망성 검사(Promising Check)**: 현재 경로가 해가 될 가능성이 있는지 검사합니다.
4.  **가지치기(Pruning)**: 만약 현재 경로가 해가 될 가능성이 없다면, 더 이상 깊이 들어가지 않고 **뒤로 돌아옵니다.**

---

## 2. 예제: N-Queens (N-퀸) 문제

N-퀸 문제는 $N \times N$ 크기의 체스판에 $N$개의 퀸을 서로 공격할 수 없도록 놓는 모든 경우의 수를 찾는 문제입니다. 퀸은 가로, 세로, 대각선으로 움직이며 공격할 수 있습니다.

### 문제 해결 과정

1.  **목표**: $N$개의 퀸을 놓는 유효한 모든 방법을 찾습니다.
2.  **상태 공간 트리**:
    * 트리의 깊이는 행(row)을 나타냅니다.
    * 1번 행부터 차례대로 퀸을 놓습니다.
    * 각 행마다 $N$개의 열(column) 중 하나에 퀸을 놓는 선택지가 있습니다.
3.  **유망성 검사**:
    * 현재 퀸을 놓을 위치가 이전에 놓인 퀸들과 서로 공격할 수 있는 위치인지 확인합니다.
    * **공격 가능 조건**:
        * **같은 열**: 같은 열에 이미 퀸이 있는가?
        * **같은 대각선**: 대각선 방향에 이미 퀸이 있는가? ($|row_1 - row_2| = |col_1 - col_2|$)
4.  **가지치기**:
    * 만약 현재 퀸을 놓을 위치가 공격 가능한 위치라면, 해당 열은 더 이상 탐색하지 않고 다음 열로 넘어갑니다.
    * 현재 행의 모든 열에 퀸을 놓을 수 없다면, 이전 행으로 **되돌아와서** 퀸의 위치를 다시 선택합니다.

### N-Queens Python 코드 예제

아래 코드는 4-Queens 문제의 해를 찾는 간단한 예제입니다.

```python
def is_safe(board, row, col):
    """현재 위치에 퀸을 놓을 수 있는지 검사하는 함수"""
    # 같은 열에 퀸이 있는지 확인
    for i in range(row):
        if board[i] == col:
            return False
    
    # 왼쪽 위 대각선 확인
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False
            
    # 오른쪽 위 대각선 확인
    for i, j in zip(range(row, -1, -1), range(col, 4)):
        if board[i] == j:
            return False
            
    return True

def solve_n_queens(board, row):
    """백트래킹을 이용하여 N-Queens 문제를 해결하는 함수"""
    # 모든 퀸을 다 놓았으면 해를 찾은 것
    if row >= 4:
        print(board)
        return

    # 현재 행의 각 열에 퀸을 놓아보기
    for col in range(4):
        if is_safe(board, row, col):
            # 퀸을 놓음 (결정)
            board[row] = col
            # 다음 행으로 넘어감 (재귀 호출)
            solve_n_queens(board, row + 1)
            # 퀸을 다시 제거 (백트래킹)
            # 이 코드는 재귀 함수가 반환될 때 자동으로 실행됨
            # 실제로 퀸을 제거하는 로직은 필요 없지만, 개념적으로는 존재함

board = [-1] * 4  # 4x4 보드, 각 행의 퀸 위치를 저장
solve_n_queens(board, 0)

## 3. Backtracking 기본형

def backtrack(current_state):
    """
    백트래킹 알고리즘의 기본 템플릿
    current_state: 현재까지의 부분적인 해
    """

    # 1. 종료 조건: 해를 찾았거나 더 이상 탐색할 필요가 없을 때
    if is_solution(current_state):
        # 해를 처리 (출력, 저장 등)
        process_solution(current_state)
        return

    # 2. 유망성 검사 (Pruning): 현재 상태가 해가 될 가능성이 없는지 확인
    if not is_promising(current_state):
        return

    # 3. 재귀 호출: 다음 상태를 생성하고 재귀적으로 탐색
    for next_option in get_options(current_state):
        # 선택: 새로운 상태를 생성
        new_state = make_a_choice(current_state, next_option)
        
        # 재귀: 다음 단계로 이동
        backtrack(new_state)
        
        # 복원 (Backtrack): 선택을 되돌리기
        # 대부분의 경우, 재귀 함수가 반환될 때 자동으로 복원됨
        undo_choice(current_state, next_option)