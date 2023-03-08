# 백준 #2252 줄 세우기
'''
    Algorithm: 위상 정렬
    Time Complexity: O(N+M)
'''
import sys
from typing import Tuple, Callable
from collections import deque


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, M = map(int, input().split())
    return N, M


def solution(N:int, M:int) -> int:
    result = []
    in_cnt = [0 for _ in range(N+1)]
    out_degree = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())

        in_cnt[b] += 1
        out_degree[a].append(b)
    
    q = deque()
    visited = [False for _ in range(N+1)]

    for i in range(1, N+1):
        if not in_cnt[i]:
            q.append(i)
            visited[i] = True
    
    while q:
        x = q.popleft()
        
        result.append(x)
        
        for nx in out_degree[x]:
            in_cnt[nx] -= 1
            if in_cnt[nx] == 0 and not visited[nx]:
                q.append(nx)
                visited[nx] = True
            
    return result


if __name__ == "__main__":
    print(*solution(*read_data()))
