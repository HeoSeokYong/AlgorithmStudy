# 백준 #19236 청소년 상어
'''
    Algorithm: 구현, 백트래킹
    Time Complexity: -
'''
import sys
from copy import deepcopy
from typing import List, Tuple, Callable

R = C = 4

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    fishes = [[None for _ in range(R)] for _ in range(C)]

    for i in range(R):
        inp = list(map(int, input().split()))

        for j in range(0, 7, 2):
            fishes[i][j // 2] = [inp[j], inp[j+1]-1]

    return fishes,


def solution(fishes:List[List[int]]) -> int:
    result = 0
    dxdy = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

    def find_fish(fishes:List[List[int]]) -> List[int]:
        fish_loc = [None for _ in range(17)]

        for i in range(R):
            for j in range(C):
                if fish := fishes[i][j]:
                    fish_loc[fish[0]] = (i, j)

        return fish_loc
    
    def move_fish(fishes:List[List[int]], shark_loc:Tuple) -> List[List[int]]:
        fish_loc = find_fish(fishes)

        # 번호 순서대로 이동
        for idx in range(1, 17):
            if fish_loc[idx]:
                x, y = fish_loc[idx]
                dir_ = fishes[x][y][1]

                for i in range(8):
                    d = (dir_ + i) % 8
                    dx, dy = dxdy[d]
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < R and 0 <= ny < C and (nx, ny) != shark_loc:
                        ndir = (dir_ + i) % 8

                        # 해당 칸에 물고기가 있는 경우
                        if nidx := fishes[nx][ny][0]: 
                            fishes[x][y], fishes[nx][ny] = fishes[nx][ny], [idx, ndir]
                            fish_loc[idx], fish_loc[nidx] = fish_loc[nidx], fish_loc[idx]
                        # 빈 칸인 경우
                        else: 
                            fishes[x][y], fishes[nx][ny] = [0, 0], [idx, ndir]
                            fish_loc[idx] = (nx, ny)

                        break

    def find_food(fishes:List[List[int]], dir_:int, sx:int, sy:int) -> List[Tuple]:
        food_cand = []

        dx, dy = dxdy[dir_]

        for mult in range(1, 4):
            nx, ny = sx + (dx * mult), sy + (dy * mult)

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                break

            if fishes[nx][ny][0]:
                food_cand.append((nx, ny))

        return food_cand

    def dfs(sx:int, sy:int, score:int, fishes:List[List[int]]):
        '''
            sx, sy : shark의 위치
            score : 먹은 물고기들의 합
            fishes : 물고기들의 정보
        '''
        nonlocal result

        nfishes = deepcopy(fishes)

        # Eat
        food, d = fishes[sx][sy]
        nfishes[sx][sy] = [0, 0]
        score += food

        # Move fish
        move_fish(nfishes, (sx, sy))
        
        # find food
        if foods := find_food(nfishes, d, sx, sy):
            for nx, ny in foods:
                dfs(nx, ny, score, nfishes)
        else:
            result = max(result, score)

    # main
    dfs(0, 0, 0, fishes)

    return result


if __name__ == "__main__":
    print(solution(*read_data()))
