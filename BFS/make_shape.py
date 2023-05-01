# 백준 #16932 모양 만들기
'''
    Algorithm: bfs
    Time Complexity: O(NM) 
'''
import sys
from typing import List, Tuple, Callable
from collections import deque


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    return N, M, arr


def solution(N:int, M:int, arr:List[int]) -> int:
    result = 0
    dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    shape_sizes = [0]

    def bfs(r:int, c:int, idx:int) -> int:
        ''' 인접한 숫자들을 그룹화 '''
        sz = 1
        q = deque([(r, c)])
        visited[r][c] = idx

        while q:
            x, y = q.popleft()    

            for dx, dy in dxdy:
                nx, ny = x + dx, y + dy

                if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and arr[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = idx
                    sz += 1

        return sz
    
    def connect(x:int, y:int) -> int:
        ''' x, y를 1로 변경했을 때 인접한 그룹 크기의 합 반환 '''
        adjs = set()

        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny]:
                adjs.add(visited[nx][ny])

        return sum(shape_sizes[adj] for adj in adjs) + 1

    # main
    idx = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]:
                shape_sizes.append(bfs(i, j, idx := idx + 1))

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                result = max(result, connect(i, j))

    return result


if __name__ == "__main__":
    print(solution(*read_data()))
