import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
K = int(input()) - 1

# heap dijkstra : (node, 거리)=시간초과
# Dijkstra는 거리가 가장 짧은 간선을 먼저 사용해야 하기에
# 기준이 거리가 되어야 하고, 따라서 (거리, node) 쌍으로 넣어주어야 한다.

dp = [INF] * V
heap = []
path = [[] for _ in range(V)]

def Dijkstra(x):
    dp[x] = 0
    heapq.heappush(heap, (0, x))

    while heap:
        wt, idx = heapq.heappop(heap)
        if dp[idx] < wt:
            continue

        for w, next in path[idx]:
            next_w = wt + w
            if next_w < dp[next]:
                dp[next] = next_w
                heapq.heappush(heap, (next_w, next))

for i in range(E):
    u, v, w = map(int, input().split())
    path[u-1].append((w, v-1))

Dijkstra(K)
for d in dp:
    print('INF' if d == INF else d)