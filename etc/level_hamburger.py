# 백준 #16974 레벨 햄버거
'''
    Algorithm: 재귀
    Time Complexity: -
'''

import sys
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, X = map(int, input().split())
    return N, X


def solution(N:int, X:int) -> int:
    hamburger = [1 for _ in range(N+1)] # 버거의 레이아웃 개수
    patty = [1 for _ in range(N+1)] # 버거의 패티 개수

    for i in range(1, N+1):
        hamburger[i] = 1 + hamburger[i-1] + 1 + hamburger[i-1] + 1
        patty[i] = 2 * patty[i-1] + 1


    def level(n:int, x:int) -> int:
        if n == 0:
            return x
        if x == 1:
            return 0
        elif x <= 1 + hamburger[n-1]:
            return level(n-1, x-1)
        elif x == 1 + hamburger[n-1] + 1:
            return patty[n-1] + 1
        elif x <= hamburger[n-1] + hamburger[n-1] + 1 + 1:	
            return patty[n-1] + 1 + level(n-1, (x-(hamburger[n-1]+2)))
        else:								
            return patty[n]

    return level(N, X)



if __name__ == "__main__":
    print(solution(*read_data()))
