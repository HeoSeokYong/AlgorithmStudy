import sys
input = sys.stdin.readline

'''
    dp: 해당 cost로 얻을 수 있는 최대 메모리
'''

n, m = map(int, input().split())
apps = [[int(a), int(b)] for a, b in zip(input().split(), input().split())]
sum_cost = sum([x[1] for x in apps])

dp = [[0] * (sum_cost+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, sum_cost+1):
        if apps[i-1][1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-apps[i-1][1]] + apps[i-1][0])

print(dp[n].index([d for d in dp[n] if d >= m][0]))