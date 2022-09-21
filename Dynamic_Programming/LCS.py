# Longest Common Subsequence
import sys
input = sys.stdin.readline

# 마지막 \n 제거 위해 strip 필요
s1 = input().strip()
s2 = input().strip()
l2, l1 = len(s2), len(s1)

# # 2차원 배열 dp
# dp = [[0] * (l2+1) for _ in range(l1+1)]

# for i in range(1, l1+1):
#     for j in range(1, l2+1):
#         if s1[i-1] == s2[j-1]:
#             dp[i][j] = dp[i-1][j-1] + 1
#         else:
#             dp[i][j] = max(dp[i][j-1], dp[i-1][j])

# print(dp[-1][-1])

# 1차원 배열 dp -> 메모리, 시간 절약
dp = [0] * l2

for i in range(l1):
    lev = 0
    for j in range(l2):
        if lev < dp[j]:
            lev = dp[j]
        elif s1[i] == s2[j]:
            dp[j] = lev + 1
print(max(dp))

