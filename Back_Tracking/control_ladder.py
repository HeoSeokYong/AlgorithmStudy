# 백준 #16565 N포커
'''
    Algorithm: brute-force, back-tracking
    Time Complexity: -

    가로선의 모든 경우의 수를 조사한다.
'''
import sys
from typing import List, Tuple, Callable
from itertools import combinations


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, M, H = map(int, input().split())
    path = [[False for _ in range(N)] for _ in range(H)]

    for _ in range(M):
        a, b = map(int, input().split())
        path[a-1][b-1] = True
        
    return N, M, H, path


def solution(N:int, M:int, H:int, path:List) -> int:

    def check(ladders) -> bool:
        flag = True
        for x, y in ladders:
            path[x][y] = True

        for i in range(N):
            y = i
            for j in range(H):
                if path[j][y]:
                    y += 1
                elif 0 <= y-1 and path[j][y-1]:
                    y -= 1
            if y != i:
                flag = False
                break

        for x, y in ladders:
            path[x][y] = False

        return flag

    ladder_cand = set((i, j) for i in range(H) for j in range(N-1))

    for i in range(H):
        for j in range(N):
            if path[i][j]:
                ladder_cand.discard((i, j))
                if j > 0:
                    ladder_cand.discard((i, j-1))
                if j < N:
                    ladder_cand.discard((i, j+1))

    if check([]):
        return 0
    
    for i in range(1, 4):
        for ladders in combinations(ladder_cand, i):
            if check(ladders):
                return i
    
    return -1
                

if __name__ == "__main__":
    print(solution(*read_data()))
