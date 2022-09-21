import sys
input = sys.stdin.readline

N, M = map(int, input().split())

table = []
for i in range(N):
    table.append(list(map(int, input().split())))

# 누적합 표 구하기
# dp 1 크게 하면 편하다.
dp = [[0] * (N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + table[i][j]
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])



