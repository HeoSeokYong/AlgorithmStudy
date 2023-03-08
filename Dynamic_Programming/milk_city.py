# 백준 #14722 우유 도시
'''
    Algorithm: dp
    Time Complexity: O(N^2) 

    dp[i][j] : 현재까지 마신 우유의 최댓값 
    현재까지 마신 우유의 수 % 3 으로 현재 마셔야 할 우유를 알 수 있다.
'''
import sys
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    city = [list(map(int, input().split())) for _ in range(N)]
    return N, city


def solution(N:int, city:List[List[int]]) -> int:
    dp = [[0 for _ in range(N)] for _ in range(N)]

    if city[0][0] == 0:
        dp[0][0] = 1
    
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + (city[i][0] == (dp[i-1][0]) % 3)
    
    for j in range(1, N):
        dp[0][j] = dp[0][j-1] + (city[0][j] == (dp[0][j-1]) % 3)

    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

            if dp[i][j] % 3 == city[i][j]:
                dp[i][j] += 1

    return dp[N-1][N-1]


if __name__ == "__main__":
    print(solution(*read_data()))
