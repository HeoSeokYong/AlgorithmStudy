# 백준 #1504 특정한 최단 경로
'''
    Algorithm: dijkstra
    Time Complexity: 
    1 - x - y - N
    1 - y - x - N
    2가지 중 더 짧은 경로가 답
'''
import sys
import heapq

input = sys.stdin.readline
INF = 1e7

def solution(N, E):
    path = {i+1:[] for i in range(N)}

    for _ in range(E):
        a, b, c = map(int, input().split())
        path[a].append((b, c))
        path[b].append((a, c))

    target1, target2 = map(int, input().split())

    def dijkstra(x):
        dist = [INF] * (N+1)
        heap = [(0, x)]
        dist[x] = 0

        while heap:
            d, n = heapq.heappop(heap)

            for dest, cost in path[n]:
                if dist[dest] > d + cost:
                    dist[dest] = d + cost
                    heapq.heappush(heap, (d+cost, dest))

        return dist
    
    dist_1 = dijkstra(1)
    dist_t1 = dijkstra(target1)
    dist_t2 = dijkstra(target2)
    
    answer = min(dist_1[target1] + dist_t1[target2] + dist_t2[N],\
                dist_1[target2] + dist_t2[target1] + dist_t1[N])

    return answer if answer < INF else -1


if __name__ == "__main__":
    N, E = map(int, input().split())

    print(solution(N, E))