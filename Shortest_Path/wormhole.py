'''
    Bellman-Ford Algorithm
'''
import sys
input = sys.stdin.readline
INF = sys.maxsize

def bf(graph, start):
    dist, pre = dict(), dict()
    for i in range(len(graph)):
        dist[i+1] = INF
        pre[i+1] = None
    dist[start] = 0

    for i in range(len(graph)-1): # V-1번 반복
        for node in graph:
            for neighbor in graph[node]:
                if dist[neighbor] > dist[node] + graph[node][neighbor]:
                   dist[neighbor] = dist[node] + graph[node][neighbor]
                pre[neighbor] = node
    

    # 음수 사이클 판별
    for node in graph:
        for neighbor in graph[node]:
            if dist[neighbor] > dist[node] + graph[node][neighbor]:
                return True
    return False

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    path = dict()
    for i in range(1, N+1):
        path[i] = dict()
    for i in range(M+W):
        S, E, T = map(int, input().split())
        if i < M:
            if E not in path[S]:
                path[S][E] = T
            else:
                path[S][E] = min(path[S][E], T)
            if S not in path[E]:
                path[E][S] = T
            else:
                path[E][S] = min(path[E][S], T)
        else:
            if E not in path[S]:
                path[S][E] = -T
            else:
                path[S][E] = min(path[S][E], -T)

    if bf(path, 1):
        print('YES')
    else:
        print('NO')