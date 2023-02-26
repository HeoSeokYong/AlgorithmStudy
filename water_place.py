# 백준 #
'''
    Algorithm: bfs
    Time Complexity: O(N + K)

'''
import sys
from typing import List, Tuple, Callable
from collections import deque

INF = 1e8 + 1e5

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, K = map(int, input().split())
    waters = list(map(int, input().split()))
    return N, K, waters


def solution(N:int, K:int, waters:List[int]) -> int:
    result = 0
    visited = set(waters)
    q = deque((w, 1) for w in waters)

    while K and q:
        x, c = q.popleft()

        for dx in [-1, 1]:
            nx = x + dx

            if -INF <= nx <= INF and nx not in visited:
                result += c
                q.append((nx, c+1))
                visited.add(nx)
                K -= 1
                if K == 0:
                    break

    return result


if __name__ == "__main__":
    print(solution(*read_data()))
