# 백준 #1261 알고스팟
'''
    Algorithm: 다익스트라
    Time Complexity: O(NMlogNM)

'''
import sys
import heapq
from typing import List, Tuple, Callable

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    M, N = map(int, input().split())
    maze = [input() for _ in range(N)]

    return N, M, maze


def solution(N: int, M: int, maze: List[str]) -> int:
    INF = float('inf')
    dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    crash = [[INF for _ in range(M)] for _ in range(N)]
    
    heap = [(0, 0, 0)] # (crash, x, y)
    crash[0][0] = 0
    
    while heap:
        c, x, y = heapq.heappop(heap)

        if x == N-1 and y == M-1:
            return c

        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if maze[nx][ny] == '1' and crash[nx][ny] > crash[x][y] + 1:
                    crash[nx][ny] = crash[x][y] + 1
                    heapq.heappush(heap, (c+1, nx, ny))
                elif maze[nx][ny] == '0' and crash[nx][ny] > crash[x][y]:
                    crash[nx][ny] = crash[x][y]
                    heapq.heappush(heap, (c, nx, ny))

    return -1


if __name__ == "__main__":
    print(solution(*read_data()))
