# 백준 #21609 상어 중학교
'''
    Algorithm: 구현, bfs
    Time Complexity: -

'''
import sys
from typing import List, Tuple, Callable, Set
from collections import deque

RAINBOW, BLACK, EMPTY = 0, -1, -2

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, M = map(int, input().split())
    grids = [list(map(int, input().split())) for _ in range(N)]
    return N, M, grids


def solution(N: int, M: int, grids: List[List[int]]) -> int:
    dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def find_block_group(grid: List[List[int]]):
        ''' bfs를 진행하고 가장 큰 블록 그룹을 반환 '''
        block_groups = []
        visited = [[False for _ in range(N)] for _ in range(N)]

        def bfs(i: int, j: int):
            ''' (i, j)부터 시작해 블록 그룹을 구하고 후처리를 한 뒤 block_groups에 추가 '''
            q = deque([(i, j)])
            color = grid[i][j]
            group = set([(i, j)])

            while q:
                x, y = q.popleft()

                for dx, dy in dxdy:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] in [color, RAINBOW] and (nx, ny) not in group:
                        group.add((nx, ny))
                        q.append((nx, ny))
            
            if len(group) >= 2:
                block_groups.append([group, -1, (N, N)])
                # 방문 처리 및 기준 블록과 무지개 블록의 수를 group과 같이 저장
                rainbow_cnt = 0
                for x, y in group:
                    if grid[x][y] != RAINBOW:
                        visited[x][y] = True
                        if (x, y) < block_groups[-1][2]:
                            block_groups[-1][2] = (x, y)
                    else:
                        rainbow_cnt += 1
                block_groups[-1][1] = rainbow_cnt


        def find_largest_group() -> Set:
            ''' 앞의 bfs에서 찾은 group들 중 조건에 맞는 가장 큰 블록 그룹을 반환 '''
            max_len = max(map(lambda x:len(x[0]), block_groups))
            # 크기가 가장 큰 블록
            cands_big = [b for b in block_groups if len(b[0]) == max_len]

            # 2개 이상이라면 무지개 블록이 가장 많은 그룹
            if len(cands_big) >= 2:
                max_rainbow = max(map(lambda x:x[1], cands_big))
                cands_rainbow = [c for c in cands_big if c[1] == max_rainbow]

                # 2개 이상이라면 기준블록이 가장 큰 그룹
                if len(cands_rainbow) >= 2:
                    return max(cands_rainbow, key=lambda x:x[2])[0]
                else:
                    return cands_rainbow[0][0]
            else:
                return cands_big[0][0]


        # find block groups
        for i in range(N):
            for j in range(N):
                if grid[i][j] > 0 and not visited[i][j]: # Normal block
                    bfs(i, j)

        # get largest block groups
        if block_groups:
            return find_largest_group()
        else:
            return []


    def auto_play(grid: List[List[int]]) -> int:
        ''' 끝날 때까지 자동으로 게임을 진행하며 얻은 점수를 반환 '''
        score = 0

        def remove_block():
            for x, y in block_group:
                grid[x][y] = EMPTY


        def gravity():
            ''' grid에 중력을 건다 '''
            for i in range(N-2, -1, -1):
                for j in range(N):
                    if grid[i][j] >= 0: # rainbow or normal block
                        # 떨어질 위치 찾기
                        x = i
                        while x+1 < N and grid[x+1][j] == -2:
                            x += 1
                        if x != i:
                            grid[x][j] = grid[i][j]
                            grid[i][j] = EMPTY

                        
        def rotate() -> List[List[int]]:
            ''' grid를 90도 반시계 방향으로 회전 '''
            rotate_grid = [[0 for _ in range(N)] for _ in range(N)]

            for i in range(N):
                for j in range(N):
                    rotate_grid[i][j] = grid[j][N-1-i]

            return rotate_grid
            

        # main
        while block_group := find_block_group(grid):
            # remove block, get points
            remove_block()
            score += len(block_group) ** 2

            # gravity
            gravity()

            # counterclock rotate & gravity
            grid = rotate()
            gravity()

        return score

    return auto_play(grids)


if __name__ == "__main__":
    print(solution(*read_data()))

