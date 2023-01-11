# 백준 #6086 최대 유량
'''
    Algorithm: Maximum flow problem
    Time Complexity: -

    try 1) 재귀 형식 -> 실패

    try 2) 알고리즘 적용 해보기 (V: node, E: edge, f: 최대 유량)

        1. 포드-풀커슨 알고리즘 (DFS) -> 156 ms
            - 시간복잡도: O((V+E)f) = (52+700)*1000 = 752,000

        2. 에드몬드-카프 알고리즘 (BFS) -> 144 ms
            - 시간복잡도: O(VE^2) = (52*700^2) = 25,480,000
            - 최악의 경우 시간복잡도는 에드몬드-카프쪽이 높지만 BFS로 쉽게 탐색하는 경우를
              DFS로는 늦게 탐색하는 경우가 있어 간선이 엄청 많은 경우가 아니면 보통 
              포드-풀커슨보다 결과가 조금 더 좋게 나온다.

        3. 디닉 알고리즘 -> 140 ms
            - 시간복잡도: O(V^2E) = (52^2 * 700) = 1,892,800
            - work 배열로 노드가 볼 간선을 기록해주는 것이 중요하다. (시간 단축을 위해)

'''
import sys
from collections import deque
from typing import List

input = sys.stdin.readline
INF = sys.maxsize
VMAX = 26 * 2 # A-Z, a-z
CASE = 3 # 1: ford-fulkerson, 2: edmonds-karp, 3: dinic
    
def ctoi(c: str) -> int:
    if c.isupper():
        return ord(c) - ord('A')
    else:
        return ord(c) - ord('a') + 26

def solution(N: int, capacity: List[List[int]], adj_list: List[List[int]]) -> int:
    flow = [[0 for _ in range(VMAX)] for _ in range(VMAX)]
    source, sink = ctoi('A'), ctoi('Z')

    def ford_fulkerson(source: int, sink: int) -> int:
        total_flow = 0

        def dfs(source, sink, visited):
            stack = deque([source])

            while stack and visited[sink] == -1:
                u = stack.pop()

                for v in adj_list[u]:
                    if capacity[u][v] - flow[u][v] > 0 and visited[v] == -1:
                        stack.append(v)
                        visited[v] = u

                        if v == sink:
                            break

            return visited[sink]

        # ford-fulkerson
        while True:
            visited = [-1 for _ in range(VMAX)]

            if dfs(source, sink, visited) == -1:
                break

            min_flow = INF

            idx = sink
            while idx != source:
                min_flow = min(min_flow, capacity[visited[idx]][idx] - flow[visited[idx]][idx])
                idx = visited[idx]

            idx = sink
            while idx != source:
                flow[visited[idx]][idx] += min_flow
                flow[idx][visited[idx]] -= min_flow
                idx = visited[idx]

            total_flow += min_flow
            
        return total_flow
    
    def edmonds_karp(source: int, sink: int) -> int:
        total_flow = 0

        def bfs(source, sink, visited):
            q = deque([source])
            
            while q and visited[sink] == -1:
                u = q.popleft()

                for v in adj_list[u]:
                    if capacity[u][v] - flow[u][v] > 0 and visited[v] == -1:
                        visited[v] = u
                        q.append(v)

                        if v == sink:
                            break
                
            return visited[sink]

        # edmonds-karp
        while True:
            visited = [-1 for _ in range(VMAX)]

            if bfs(source, sink, visited) == -1:
                break

            min_flow = INF

            idx = sink
            while idx != source:
                min_flow = min(min_flow, capacity[visited[idx]][idx] - flow[visited[idx]][idx])
                idx = visited[idx]

            idx = sink
            while idx != source:
                flow[visited[idx]][idx] += min_flow
                flow[idx][visited[idx]] -= min_flow
                idx = visited[idx]

            total_flow += min_flow

        return total_flow

    def dinic(source: int, sink: int) -> int:
        total_flow = 0
        level_graph = [-1 for _ in range(VMAX)]

        def bfs(source: int, sink: int) -> List[List[int]]:
            ''' 주어진 네트워크의 레벨 그래프를 반환 '''
            level_graph[source] = 0
            q = deque([source])

            while q:
                u = q.popleft()

                for v in adj_list[u]:
                    if level_graph[v] == -1 and capacity[u][v] - flow[u][v] > 0:
                        level_graph[v] = level_graph[u] + 1
                        q.append(v)

            return level_graph[sink] != -1

        def dfs(u: int, cur_flow: int) -> int:
            ''' (재귀) 레벨 그래프와 차단 유량을 통해 구한 현재 네트워크의 유량을 반환 '''
            if u == sink:
                return cur_flow

            for i in range(work[u], len(adj_list[u])):
                v = adj_list[u][i]

                if level_graph[v] == level_graph[u] + 1 and capacity[u][v] - flow[u][v] > 0:
                    res = dfs(v, min(cur_flow, capacity[u][v] - flow[u][v]))

                    if res > 0:
                        flow[u][v] += res
                        flow[v][u] -= res
                        work[u] = i

                        return res

            work[u] = len(adj_list[u])
            return 0
        
        # dinic
        while bfs(source, sink): # Make level graph
            work = [0 for _ in range(VMAX)]

            while cur_flow := dfs(source, INF): # sum flow
                total_flow += cur_flow
            
            level_graph = [-1 for _ in range(VMAX)]

        return total_flow
    
    # main
    match CASE:
        case 1:
            return ford_fulkerson(source, sink)
        case 2:
            return edmonds_karp(source, sink)
        case 3:
            return dinic(source, sink)
    

if __name__ == "__main__":
    N = int(input())
    capacity = [[0 for _ in range(VMAX)] for _ in range(VMAX)]
    adj_list = [[] for _ in range(VMAX)]
    
    for _ in range(N):
        a, b, f = input().split()

        a = ctoi(a)
        b = ctoi(b)

        capacity[a][b] += int(f)
        capacity[b][a] += int(f)

        adj_list[a].append(b)
        adj_list[b].append(a)

    print(solution(N, capacity, adj_list))