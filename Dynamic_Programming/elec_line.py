import sys 
input = sys.stdin.readline

n = int(input())

elines = []
for i in range(n):
    elines.append(list(map(int, input().split())))
    
elines.sort()

dp = [0] * n
for i in range(n):
    for j in range(i):
        if elines[i][1] > elines[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(n - max(dp))