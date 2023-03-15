# 백준 #2482 색상환
'''
    Algorithm: dp
    Time Complexity: O(NK)

    dp[i][j] : i개의 색 중에서 j개의 색을 고르는 경우의 수
        i개의 색 중 i-1번째는 고르지 못함.
        따라서 i-2개의 색 중 j-1개를 고르는 경우와, (j번째 색을 고르는 경우)
        i-1개의 색 중 j개를 고르는 경우를 더해주면 되겠다. (j번째 색을 고르지 않는 경우)
        => dp[i][j] = dp[i-2][j-1] + dp[i-1][j]

        마지막 N번째의 경우 N-1과 첫번째 수를 고르지 못하기 때문에,
        => dp[N][j] = dp[N-3][j-1] + dp[N-1][j]
'''
import sys
from typing import Tuple, Callable

MOD = 10**9 + 3

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    K = int(input())
    return N, K


def solution(N:int, K:int) -> int:
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

    for n in range(N+1):
        dp[n][0] = 1
        dp[n][1] = n

    for n in range(2, N+1):
        for k in range(2, K+1):
            dp[n][k] = (dp[n-2][k-1] + dp[n-1][k]) % MOD 

    for k in range(2, K+1):
        dp[N][k] = (dp[N-3][k-1] + dp[N-1][k]) % MOD

    return dp[N][K]


if __name__ == "__main__":
    print(solution(*read_data()))
