# 백준 #1563 개근상
'''
    Algorithm: dp
    Time Complexity: -

    dp로 해보자. (n x 3 행렬)
    - bottom-up 은 도저히 못하겠다.
    - top-down으로 하자.

'''
import sys
from typing import Tuple, Callable

sys.setrecursionlimit(10**7)
     
def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    return N,


def solution(N: int) -> int:
    dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(N+1)]
    
    def attendance(day:int, late:int, absent:int) -> int:
        if late == 2 or absent == 3:
            return 0

        if day == N:
            return 1

        if dp[day][late][absent] == 0:
            # O
            dp[day][late][absent] += attendance(day+1, late, 0)
            # L
            dp[day][late][absent] += attendance(day+1, late+1, 0)
            # A
            dp[day][late][absent] += attendance(day+1, late, absent+1)

        return dp[day][late][absent] % 1000000

    return attendance(0, 0, 0)


if __name__ == "__main__":
    print(solution(*read_data()))

