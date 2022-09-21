# Longest Increasing Subsequnce
import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

# dp = [0] * N
# for i in range(N):
#     dp[i] = 1
#     for j in range(i):
#          if seq[j] < seq[i]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(max(dp))

# with binary search
lis = [seq[0]]

def binary_search(left, right, target):
    while left < right:
        mid = (left + right) // 2
        if lis[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right

i = 1
while i < N:
    if lis[-1] < seq[i]:
        lis.append(seq[i])
    else:
        idx = binary_search(0, len(lis), seq[i])
        lis[idx] = seq[i]
    i += 1
print(len(lis))