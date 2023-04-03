# 백준 #14578 영훈이의 색칠공부
'''
    Algorithm: dp, 수학
    Time Complexity: O(N)
    
    1x1 : 0
    2x2 : 2 = 2! x (1x1)
    3x3 : 12 = 3! x (2x1)

    - 교란 수열 문제라고 한다.
'''
import sys
from typing import Tuple, Callable

MOD = int(1e9) + 7

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    return N,


def solution(N:int) -> int:
    dp = [0 for _ in range(N+2)]
    dp[2] = 1

    for i in range(2, N):
        dp[i+1] = (i * (dp[i]+dp[i-1])) % MOD

    res = 1
    for i in range(2, N+1):
        res = (res * i) % MOD

    return (res * dp[N]) % MOD


if __name__ == "__main__":
    print(solution(*read_data()))
