# 백준 #1774 우주신과의 교감
'''
    Algorithm: mst, prim algorithm
    Time Complexity: O(N^2)

'''
import sys
import heapq
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, M = map(int, input().split())
    loc_god = [tuple(map(int, input().split())) for _ in range(N)]
    connected = [tuple(map(int, input().split())) for _ in range(M)]
    return N, M, loc_god, connected


def solution(N:int, M:int, loc_god:List[Tuple], connected:List[Tuple]) -> int:
    result = 0
    INF = sys.maxsize

    path = [[INF for _ in range(N)] for _ in range(N)]

    def get_dist(A:Tuple, B:Tuple):
        return ((A[0]-B[0])**2 + (A[1]-B[1])**2) ** (1/2)
    

    for i in range(N):
        for j in range(i+1, N):
            path[i][j] = path[j][i] = get_dist(loc_god[i], loc_god[j])

    for x, y in connected:
        path[x-1][y-1] = path[y-1][x-1] = 0

    heap = [(0, 0)]
    visited = [False for _ in range(N)]

    while heap:
        cost, node = heapq.heappop(heap)

        if visited[node]:
            continue

        result += cost
        visited[node] = True

        for i in range(N):
            if not visited[i]:
                heapq.heappush(heap, (path[node][i], i))

    return f'%.2f' %(result)


if __name__ == "__main__":
    print(solution(*read_data()))
