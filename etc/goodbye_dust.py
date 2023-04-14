# 백준 #17144 미세먼지 안녕!
'''
    Algorithm: 구현
    Time Complexity: O(RCT)

'''
import sys
from typing import List, Tuple, Callable

FURIFIER = -1

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    R, C, T = map(int, input().split())
    house = [list(map(int, input().split())) for _ in range(R)]
    return R, C, T, house


def solution(R:int, C:int, T:int, house:List[List[int]]) -> int:
    drdc = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    air_cleaner = [i for i in range(R) if house[i][0] == FURIFIER]

    def spread():
        var = [[0 for _ in range(C)] for _ in range(R)]

        for r in range(R):
            for c in range(C):
                if house[r][c] > 0:
                    if dust := house[r][c] // 5:
                        for dr, dc in drdc:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < R and 0 <= nc < C and house[nr][nc] != FURIFIER:                            
                                var[nr][nc] += dust
                                var[r][c] -= dust

        for r in range(R):
            for c in range(C):
                house[r][c] += var[r][c]


    def air_clean():
        # 상부
        loc = air_cleaner[0]

        # left
        for r in range(loc-1, 0, -1):
            house[r][0] = house[r-1][0]
        # up
        for c in range(C-1):
            house[0][c] = house[0][c+1]
        # right
        for r in range(loc):
            house[r][-1] = house[r+1][-1]
        # down
        for c in range(C-1, 1, -1):
            house[loc][c] = house[loc][c-1]
        
        house[loc][1] = 0

        # 하부
        loc = air_cleaner[1]

        # left
        for r in range(loc+1, R-1):
            house[r][0] = house[r+1][0]
        # down
        for c in range(C-1):
            house[-1][c] = house[-1][c+1]
        # right
        for r in range(R-1, loc, -1):
            house[r][-1] = house[r-1][-1]
        # up
        for c in range(C-1, 1, -1):
            house[loc][c] = house[loc][c-1]
        
        house[loc][1] = 0

    # main
    for _ in range(T):
        spread()
        air_clean()
    
    return sum(map(sum, house)) + 2


if __name__ == "__main__":
    print(solution(*read_data()))
