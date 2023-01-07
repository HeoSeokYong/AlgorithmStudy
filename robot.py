# 백준 #1726 로봇
'''
    Algorithm: bfs
    Time Complexity: O(MN)

    아 k는 1~3 이다.
'''
import sys
from typing import List, Tuple
from collections import deque

input = sys.stdin.readline
dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solution(M: int, N: int, factory: List[List[int]], start: Tuple, end: Tuple) -> int:
    
    def dir_mapping(d: int) -> int:
        return [-1, 0, 2, 1, 3][d]
    
    result = 0
    visited = [[[False for _ in range(4)] for _ in range(N)] for _ in range(M)]

    start = (start[0]-1, start[1]-1, dir_mapping(start[2]))
    end = (end[0]-1, end[1]-1, dir_mapping(end[2]))

    q = deque([start]) # (x, y, 방향)
    visited[start[0]][start[1]][start[2]] = True
    
    while q:
        for _ in range(len(q)):
            x, y, d = q.popleft()

            if (x, y, d) == end:
                return result
            
            dx, dy = dxdy[d]

            # Comm 1
            for k in range(1, 4):
                nx, ny = x + k*dx, y + k*dy

                if 0 <= nx < M and 0 <= ny < N:
                    if factory[nx][ny] == 1:
                        break

                    if not visited[nx][ny][d]:
                        visited[nx][ny][d] = True
                        q.append((nx, ny, d))

            # Comm 2
            for dd in [-1, 1]:
                nd = (d + dd) % 4
                
                if not visited[x][y][nd]:
                    visited[x][y][nd] = True
                    q.append((x, y, nd))
        
        result += 1

    return -1


if __name__ == "__main__":
    M, N = map(int, input().split())
    factory = [list(map(int, input().split())) for _ in range(M)]
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    
    print(solution(M, N, factory, start, end))