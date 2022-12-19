# 백준 #1738 골목길
'''
    Algorithm: bellman-ford
    Time Complexity: O(NM) ?

    음수가 포함된 최단 경로 찾기 => 벨만-포드 알고리즘
    무조건 콘도까지 가는 경로는 있는 듯 하다.
    
    최적의 경로가 존재하지 않는 경우: (무한 돈복사가 가능한 경우)
        - 양의 사이클이 존재하며(돈을 증가시키는), 
          그 사이클이 start -> 콘도까지의 경로에 포함되어 있을 때
'''
import sys
from collections import deque
from typing import List

input = sys.stdin.readline
INF = sys.maxsize

def solution(N: int, M: int) -> List[int]:
    alley = [[] for _ in range(N+1)]
    pre = [None for _ in range(N+1)] # 각 골목길의 직전 골목길 저장

    def bellman_ford(start: int) -> int:
        ''' 사이클이 있을 경우 포함되는 노드 1개, 없을 경우 None을 리턴 '''
        dist = [-INF for _ in range(N+1)] # dist[i] : start에서 i까지 가는 비용
        
        dist[start] = 0
        
        for _ in range(N-1): 
            for node in range(1, N+1):
                for dest, cost in alley[node]:
                    if dist[dest] < dist[node] + cost:
                        dist[dest] = dist[node] + cost
                        pre[dest] = node

        # 양의 사이클 판별: 사이클을 만드는 노드 한개를 리턴
        for node in range(1, N+1): 
            for dest, cost in alley[node]:
                if dist[dest] < dist[node] + cost:
                    return node

        return 
    
    def is_copy_money(node: int) -> bool:
        ''' 최적의 경로 확인: 사이클에 존재하는 노드가 목적지 N까지의 경로가 있는 지 확인 '''
        q = deque([node])
        visited = set([node])

        # 양의 사이클이 존재하고 콘도까지 가는 경로가 있다면 True 리턴
        while q:
            node = q.popleft()

            for dest, _ in alley[node]:
                if dest == N:
                    return True
                
                if dest not in visited:
                    q.append(dest)
                    visited.add(dest)

        # 사이클이 존재하지만 콘도랑은 관련이 없을 경우 False 리턴
        return False

    def get_path(start):
        ''' 코레스코 콘도의 위치 N부터 start까지 역으로 탐색 '''
        result = [N]

        while result[-1] != start:
            result.append(pre[result[-1]])

        return reversed(result)


    for _ in range(M):
        u, v, w = map(int, input().split())
        alley[u].append((v, w))
    
    bf = bellman_ford(1)

    if bf and is_copy_money(bf):
        return [-1]
    
    return get_path(1)


if __name__ == "__main__":
    N, M = map(int, input().split())

    print(*solution(N, M))