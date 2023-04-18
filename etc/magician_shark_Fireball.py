# 백준 #20056 마법사 상어와 파이어볼
'''
    Algorithm: 구현
    Time Complexity: -

    소수점은 내림해야 한다.
'''
import sys
from typing import List, Tuple, Callable, NoReturn


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, M, K = map(int, input().split())
    fireballs = []

    for _ in range(M):
        r, c, m, s, d = map(int, input().split())
        fireballs.append((r-1, c-1, m, s, d))

    return N, M, K, fireballs


def solution(N:int, M:int, K:int, fireballs:List[Tuple]) -> int:
    drdc = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    
    def fire_ball() -> NoReturn:
        grid = [[[] for _ in range(N)] for _ in range(N)]

        # Move fireball 
        while fireballs:
            r, c, m, s, d = fireballs.pop()

            dr, dc = drdc[d]

            nr = (r + dr * s) % N
            nc = (c + dc * s) % N

            grid[nr][nc].append((m, s, d))
        
        # Fireball fusion
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    if len(grid[i][j]) == 1:
                        m, s, d = grid[i][j][0]
                        fireballs.append((i, j, m, s, d))
                    else:
                        dir_flag = True
                        dir_type = grid[i][j][0][2] % 2

                        sum_m, sum_s = 0, 0

                        for m, s, d in grid[i][j]:
                            sum_m += m
                            sum_s += s
                            if d % 2 != dir_type:
                                dir_flag = False

                        if sum_m // 5:
                            for nd in [0, 2, 4, 6] if dir_flag else [1, 3, 5, 7]:
                                fireballs.append((i, j, sum_m//5, sum_s//len(grid[i][j]), nd))
    
    # main
    for _ in range(K):
        fire_ball()
        
    return sum(f[2] for f in fireballs)


if __name__ == "__main__":
    print(solution(*read_data()))
