# 백준 #28019 산지니의 여행계획 (푸는 중...)
'''
    Algorithm: MST(max) - prim, dfs
    Time Complexity: 

    도로는 최소, 길이의 합은 최대 -> MST(max),
    dfs를 통해 최적의 경로를 구해 운전 거리를 최대한 줄여보자.

    MST 로 구한 경로 -> DAG
    출발지에서 시작해서 제일 비싼 경로를 제외하고 모두 두번씩 들린다.
        => 시작점부터 리프 노드까지의 경로 중 제일 비싼 경로를 찾자.
'''
import sys
import heapq
from collections import defaultdict
from typing import List, Tuple, Callable

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, M = map(int, input().split())
    path = [defaultdict(int) for _ in range(N)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        path[a-1][b-1] = path[b-1][a-1] = min(path[a-1][b-1], c)

    starting_point = int(input()) - 1

    return N, path, starting_point


def solution(N:int, path:List[List[int]], starting_point:int) -> int:
    result = 0
    itinerary = [[] for _ in range(N)]
    visited = [False for _ in range(N)]
    heap = []

    def dfs(city:int) -> int: # O(N-1)
        ''' 제일 깊은 경로의 길이의 합을 반환 '''
        stack = [(city, 0)]
        main_route = 0

        while stack:
            node, dist = stack.pop()
            
            if main_route < dist:
                main_route = dist

            for dest, cost in itinerary[node]:
                stack.append((dest, dist + cost))

        return main_route

    # main
    heappush = heapq.heappush
    heappop = heapq.heappop

    for dest, cost in path[starting_point].items(): # O(M)
        heappush(heap, (-cost, dest, starting_point))

    visited[starting_point] = True
    
    while heap: # O(NlogN)
        cost, city, prev_city = heappop(heap)

        if visited[city]:
            continue

        itinerary[prev_city].append((city, -cost))
        result -= (2 * cost)
        visited[city] = True

        for dest, cost in path[city].items():
            if not visited[dest]:
                heappush(heap, (-cost, dest, city))

    return result - dfs(starting_point)


if __name__ == "__main__":
    print(solution(*read_data()))
