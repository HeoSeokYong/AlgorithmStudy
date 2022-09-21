import sys
input = sys.stdin.readline

N = int(input())
cost = []
for i in range(N):
    cost.append(list(map(int, input().split())))

dp = [[0] * 3 for _ in range(N)]
for i in range(N):
    for j in range(3): # rgb
        if i == 0:
            dp[i][j] = cost[i][j]
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j-2]) + cost[i][j]
print(min(dp[-1]))
        