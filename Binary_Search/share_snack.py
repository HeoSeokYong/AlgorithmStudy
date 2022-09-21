import sys
input = sys.stdin.readline

m, n = list(map(int, input().split()))
snacks = list(map(int, input().split()))
snacks.sort()

answer = 0
left = 0
right = snacks[-1]

while left <= right:
    mid = (left+right) // 2
    if mid==0:
        break
    if sum([s//mid for s in snacks]) >= m:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1

print(answer)