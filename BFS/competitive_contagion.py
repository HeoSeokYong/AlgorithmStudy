# 백준 #18405 경쟁적 전염
'''
    Algorithm: bfs
    Time Complexity: O(SV) / V: virus의 갯수

'''
import sys
from collections import deque
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, K = map(int, input().split())
    tube = [list(map(int, input().split())) for _ in range(N)]
    S, X, Y = map(int, input().split())
    return N, K, tube, S+1, X-1, Y-1


def solution(N:int, K:int, tube:List[List[int]], S:int, X:int, Y:int) -> int:
    virus = [deque() for _ in range(K+1)]
    dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(N):
        for j in range(N):
            if tube[i][j] != 0:
                virus[tube[i][j]].append((i, j))
    
    while S := S - 1:
        if tube[X][Y]:
            break
        
        for vrs_idx in range(1, K+1):
            for _ in range(len(virus[vrs_idx])):
                x, y = virus[vrs_idx].popleft()

                for dx, dy in dxdy:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and tube[nx][ny] == 0:
                        tube[nx][ny] = vrs_idx
                        virus[vrs_idx].append((nx, ny))

    return tube[X][Y]


if __name__ == "__main__":
    print(solution(*read_data()))
