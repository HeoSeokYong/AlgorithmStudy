# 백준 #2573 빙산
'''
    Algorithm: bfs
    Time Complexity: -

'''
import sys
from collections import deque
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, M = map(int, input().split())
    ocean = [list(map(int, input().split())) for _ in range(N)]
    return N, M, ocean


def solution(N:int, M:int, ocean:List[List[int]]) -> int:
    year = 0
    dxdy = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    melt_info = [[0 for _ in range(M)] for _ in range(N)]
    icebergs = deque()

    def split_check(i:int, j:int):
        q = deque([(i, j)])
        visited = set([(i, j)])

        while q:
            x, y = q.popleft()

            for dx, dy in dxdy:
                nx, ny = x + dx, y + dy

                if 0 <= nx < N and 0 <= ny < M and ocean[nx][ny] != 0 and (nx, ny) not in visited:
                    q.append((nx, ny))
                    visited.add((nx, ny))
                    
        if len(icebergs) == len(visited):
            return True
        else:
            return False

    # main
    for i in range(N):
        for j in range(M):
            if ocean[i][j] != 0: 
                icebergs.append((i, j))     
                for dx, dy in dxdy:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < N and 0 <= ny < M and ocean[nx][ny] == 0:
                        melt_info[i][j] += 1

    while icebergs and split_check(*icebergs[0]):
        melted = []

        for _ in range(len(icebergs)):
            x, y = icebergs.popleft()

            if ocean[x][y] > melt_info[x][y]:
                ocean[x][y] -= melt_info[x][y]
                icebergs.append((x, y))
            else:
                melted.append((x, y))
        
        for x, y in melted:
            ocean[x][y] = 0
            for dx, dy in dxdy:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    melt_info[nx][ny] += 1

        year += 1

    return year if icebergs else 0


if __name__ == "__main__":
    print(solution(*read_data()))
