# 백준 #12865 평범한 배낭
'''
    Algorithm: dp
    Time Complexity:O(NK)

    기본 dp 배낭 문제
'''
import sys

input = sys.stdin.readline

def solution2(N: int, K: int) -> int:
    # 1차원 dp -> dp[i] = 배낭의 무게가 i일 때 가치합의 최대값
    items = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [0 for _ in range(K+1)]

    for w, v in items:
        for i in range(K - w, -1, -1):
            dp[i + w] = max(dp[i + w], dp[i] + v)

    return dp[K]

def solution(N: int, K: int) -> int:
    # 2차원 dp
    items = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

    for i in range(N+1):
        for j in range(K+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif items[i-1][0] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i-1][0]] + items[i-1][1])

    return dp[N][K]


if __name__ == "__main__":
    N, K = map(int, input().split())

    print(solution(N, K))