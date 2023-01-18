# 백준 #16946 벽 부수고 이동하기 4
'''
    Algorithm: bfs
    Time Complexity: O(NM)

    먼저 빈칸에서 bfs를 해서 만나는 벽의 카운트를 늘려가는 식으로 한다.
'''
import sys
from typing import List, Tuple, Callable
from collections import deque

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, M = map(int, input().split())
    board = [list(map(int, list(input()))) for _ in range(N)]

    return N, M, board


def solution(N: int, M: int, board: List[str]) -> List[str]:
    dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False for _ in range(M)] for _ in range(N)]

    def bfs(a, b):
        q = deque([(a, b)])
        visited[a][b] = True
        walls = set()
        empty_cnt = 0

        while q:
            x, y = q.popleft()
            empty_cnt += 1

            for dx, dy in dxdy:
                nx, ny = x + dx, y + dy

                if 0 <= nx < N and 0 <= ny < M:
                    if board[nx][ny] == 0 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))

                    elif board[nx][ny] > 0:
                        # 만나는 벽들을 저장
                        walls.add((nx, ny))

        for x, y in walls:
            board[x][y] += empty_cnt


    for i in range(N):
        for j in range(M):
            if board[i][j] == 0 and not visited[i][j]:
                bfs(i, j)

    return ["".join(map(lambda x: str(x%10), b)) for b in board]


if __name__ == "__main__":
    print(*solution(*read_data()), sep='\n')