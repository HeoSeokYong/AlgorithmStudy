# 백준 #1922 네트워크 연결
'''
    Algorithm: MST - prim algorithm
    Time Complexity: O(MlogN)

'''
import sys
import heapq
from typing import List, Tuple

input = sys.stdin.readline

def solution(N: int, M: int, path: List[List[Tuple]]) -> int:
    result = 0
    connected = [False for _ in range(N+1)]

    heap = [(0, 1)]

    while heap:
        cost, computer = heapq.heappop(heap)

        if connected[computer]:
            continue
        
        connected[computer] = True
        result += cost

        for w, v in path[computer]:
            if not connected[w]:
                heapq.heappush(heap, (v, w))

    return result


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    path = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        path[a].append((b, c))
        path[b].append((a, c))

    print(solution(N, M, path))