# 백준 #20058 마법사 상어와 파이어스톰
'''
    Algorithm: 구현, bfs
    Time Complexity: -
'''
import sys
from collections import deque

input = sys.stdin.readline

def solution(N: int, Q: int, ice: list[list[int]], level: list[int]) -> list[int]:
    dxdy = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def fire_storm(ice: list[list[int]], l: int) -> list[int]:
        ''' Magic: Fire Storm '''

        def storm(l: int) -> list[list[int]]:
            ''' Fire Storm: storm '''
            after_storm = [[0 for _ in range(2**N)] for _ in range(2**N)]
            lev = 2 ** l

            for i in range(0, 2**N, lev):
                for j in range(0, 2**N, lev):
                    for r in range(lev):
                        for c in range(lev):
                            after_storm[i+r][j+c] = ice[i + lev - c - 1][j + r]

            return after_storm
        
        def fire() -> None:
            ''' Fire Storm: fire '''
            fire_cand = []
            for x in range(2**N):
                for y in range(2**N):
                    if ice[x][y] > 0:
                        near = 0
                        for dx, dy in dxdy:
                            nx, ny = x + dx, y + dy

                            if 0 <= nx < 2**N and 0 <= ny < 2**N and ice[nx][ny] > 0:
                                near +=1
                        if near < 3:
                            fire_cand.append((x, y))

            for r, c in fire_cand:
                ice[r][c] -= 1

        ice = storm(l)
        fire()

        return ice

    def get_result(ice: list[list[int]]) -> list[int]:
        ''' 1. 남아있는 얼음의 합, 2. 가장 큰 얼음 덩어리의 크기 반환 '''
        SUMICE, MAXICE = 0, 0
        visited = [[False for _ in range(2**N)] for _ in range(2**N)]

        def sum_of_ice() -> int:
            return sum([sum(ic) for ic in ice])

        def get_iceblock(r: int, c: int) -> int:
            ''' bfs: r, c의 점을 포함하는 얼음 덩어리의 크기 반환 '''
            siz = 1
            q = deque([(r, c)])
            visited[r][c] = True

            while q:
                x, y = q.popleft()
                
                for dx, dy in dxdy:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < 2**N and 0 <= ny < 2**N and ice[nx][ny] > 0 and not visited[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        siz += 1
                        
            return siz

        SUMICE = sum_of_ice()
        MAXICE = max([get_iceblock(r, c) for r in range(2**N) for c in range(2**N) if not visited[r][c] and ice[r][c] > 0], default=0)

        return [SUMICE, MAXICE]

    for l in level:
        ice = fire_storm(ice, l)
    
    return get_result(ice)


if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(2**N)]
    L = list(map(int, input().split()))

    print(*solution(N, Q, A, L), sep='\n')