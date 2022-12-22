# 백준 #1106 호텔
'''
    Algorithm: dp
    Time Complexity: O(NC)

'''
import sys

input = sys.stdin.readline

def solution(C: int, N: int) -> int:
    c_range = 100*C + 1
    ad_costs = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [[0 for _ in range(c_range)] for _ in range(N+1)]

    for i in range(N+1):
        for j in range(c_range):
            if i == 0 or j == 0:
                continue
            elif j < ad_costs[i-1][0]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-ad_costs[i-1][0]] + ad_costs[i-1][1])

    for i in range(c_range):
        if dp[-1][i] >= C:
            return i


if __name__ == "__main__":
    C, N = map(int, input().split())

    print(solution(C, N))