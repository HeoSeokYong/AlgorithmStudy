import sys
input = sys.stdin.readline
INF = sys.maxsize

N, K = map(int, input().split())

# Use dijkstra with queue
q = [N]
dp = [INF] * 100001
dp[N] = 0

while q:
    cur = q.pop(0)
    if cur == K:
        print(dp[cur])
        break
    
    for i in range(3):
        next, tim = 0, 0
        if i == 0: # tp
            next = 2*cur
        else:
            next = cur + (-1)**(i)
            tim = 1
        if 0 <= next <= 100000 and dp[next] > dp[cur] + tim:
            q.append(next)
            dp[next] = dp[cur] + tim


# from collections import deque

# n, k = map(int, input().split())
# q = deque([(n,0)])
# visited = [0]*100001
# visited[n] = 1
# while q:
#     x, lev = q.popleft()
#     if x == k:
#         break
#     if 2*x <= 100000 and not visited[2*x]:
#         q.append((2*x, lev+1))
#         visited[2*x] = 1
#     if 0 <= x-1 < 100001 and not visited[x-1]:
#         q.append((x-1, lev+1))
#         visited[x-1] = 1
#     if 0 < x+1 < 100001 and not visited[x+1]:
#         q.append((x+1, lev+1))
#         visited[x+1] = 1
        
# print(lev)
