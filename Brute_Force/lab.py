# 백준 #14502 연구소
'''
    Algorithm: brute-force, bfs
    Time Complexity: O(CN^2) {C = combinations(N^2, 3)}

    3개의 벽
    조합 사용해보자.
'''
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

def solution(N: int, M: int) -> int:
    emptys, virus = [], []
    safe_zone, result = -3, 0
    maps = [[0 for _ in range(M)] for _ in range(N)]
    dxdy = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    # data input
    for i in range(N):
        inp = list(map(int, input().split()))
        for j in range(M):
            maps[i][j] = inp[j]

            if inp[j] == 0:
                emptys.append((i, j))
                safe_zone += 1

            elif inp[j] == 2:
                virus.append((i,j))

    # combinations
    for walls in combinations(emptys, 3):
        q = deque(virus)
        visited = set(virus)
        visited.update(walls)
        infected = 0
        
        while q:
            x, y = q.popleft()

            if safe_zone - infected < result:
                break

            for dx, dy in dxdy:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny))
                    infected += 1

        result = max(result, safe_zone - infected)

    return result


if __name__ == "__main__":
    N, M = map(int, input().split())

    print(solution(N, M))