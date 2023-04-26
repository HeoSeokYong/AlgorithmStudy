# 백준 #20057 마법사 상어와 토네이도
'''
    Algorithm: 구현
    Time Complexity: -
'''
import sys
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    return N, grid


def solution(N:int, grid:List[List[int]]) -> int:
    out_sand = 0
    dxdy = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    diag_dxdy = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    side_percent = [0.07, 0.02]

    tornado = {'loc': (N//2, N//2), 'dir': {'idx': 0, 'cnt': 0, 'lim': 1, 'turn_cnt': 0}}

    while True:
        x, y = tornado['loc']
        dx, dy = dxdy[tornado['dir']['idx']]
        nx, ny = x + dx, y + dy
        
        if sand := grid[nx][ny]:
            # 진행 방향의 양 옆
            for side in range((tornado['dir']['idx']+1) % 2, 4, 2):
                # 토네이도의 방향 인덱스가 짝수면 홀수 인덱스들이 사이드가 된다.(반대도 동일)
                ndx, ndy = dxdy[side]

                for m in range(1, 3):
                    nnx, nny = nx + (ndx*m), ny + (ndy*m)

                    move_sand = int(grid[nx][ny] * side_percent[m-1])
                    sand -= move_sand

                    if 0 <= nnx < N and 0 <= nny < N:
                        grid[nnx][nny] += move_sand
                    else:
                        out_sand += move_sand

            # 대각 방향
            for ndx, ndy in diag_dxdy:
                nnx, nny = nx + ndx, ny + ndy
                m = 0.1 if ndx == dx or ndy == dy else 0.01

                move_sand = int(grid[nx][ny] * m)
                sand -= move_sand

                if 0 <= nnx < N and 0 <= nny < N:
                    grid[nnx][nny] += move_sand
                else:
                    out_sand += move_sand
                
            # 진행 방향
            nnx, nny = nx + (2*dx), ny + (2*dy)
            
            move_sand = int(grid[nx][ny] * 0.05)
            sand -= move_sand
            
            if 0 <= nnx < N and 0 <= nny < N:
                grid[nnx][nny] += move_sand
            else:
                out_sand += move_sand

            # alpha
            nnx, nny = nx + dx, ny + dy

            if 0 <= nnx < N and 0 <= nny < N:
                grid[nnx][nny] += sand
            else:
                out_sand += sand

            grid[nx][ny] = 0

        if x == 0 and y == 0:
            break

        tornado['loc'] = (nx, ny)
        tornado['dir']['cnt'] += 1

        # 진행 방향 전환
        if tornado['dir']['cnt'] == tornado['dir']['lim']:
            tornado['dir']['cnt'] = 0
            tornado['dir']['turn_cnt'] += 1
            tornado['dir']['idx'] = (tornado['dir']['idx'] + 1) % 4

            if tornado['dir']['turn_cnt'] == 2:
                tornado['dir']['turn_cnt'] = 0
                tornado['dir']['lim'] += 1

    return out_sand


if __name__ == "__main__":
    print(solution(*read_data()))
