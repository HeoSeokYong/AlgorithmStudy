import sys
import heapq
input = sys.stdin.readline
INF = 1e6
'''
    Dijkstra를 통해 X에서 각 학생들의 집으로 가는 최단거리와
    reverse path를 통해 다른집에서 X로 가는 최단거리를 계산
'''
n, m, target = map(int, input().split())
path = {i+1:[] for i in range(n)}
reverse_path = {i+1:[] for i in range(n)}
result = [0] * (n+1)

def Dijkstra(x, path):
    dp = [INF] * (n+1)
    dp[x] = 0

    heap = []
    heapq.heappush(heap, (0, x))

    while heap:
        tim, dest = heapq.heappop(heap)
        if dp[dest] < tim:
            continue
        
        for t, d in path[dest]:
            next_t = tim + t
            if next_t < dp[d]:
                dp[d] = next_t
                heapq.heappush(heap, (next_t, d))

    return dp

for i in range(m):
    a, b, w = map(int, input().split())
    path[a].append((w, b))
    reverse_path[b].append((w, a))

go = Dijkstra(target, path)
back = Dijkstra(target, reverse_path)

for i in range(n):
    result[i+1] = go[i+1] + back[i+1]
    
print(max(result))
