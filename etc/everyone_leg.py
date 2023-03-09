# 백준 #17352 여러분의 다리가 되어 드리겠습니다!
'''
    Algorithm: 분리 집합
    Time Complexity: -

'''
import sys
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    return N,


def solution(N:int) -> int:
    connected = [False for _ in range(N+1)]
    parents = [i for i in range(N+1)]
    
    def find(x:int) -> int:
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x:int, y:int):
        px = find(x)
        py = find(y)

        parents[max(px, py)] = min(px, py)
        connected[max(px, py)] = True

    # main
    for _ in range(N-2):
        a, b = map(int, input().split())
        if find(a) != find(b):
            union(a,b)

    return [i for i in range(1, N+1) if not connected[i]]


if __name__ == "__main__":
    print(*solution(*read_data()))
