# 백준 #20040 사이클 게임
'''
    Algorithm: 분리집합
    Time Complexity: -

'''
import sys
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, M = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(M)]
    return N, M, points


def solution(N:int, M:int, points:List[Tuple]) -> int:
    turn = 1
    parent = [i for i in range(N)]

    def find(p1:int) -> int:
        while p1 != parent[p1]:
            p1 = parent[p1]
        return p1

    def union(p1:int, p2:int):
        parent1 = find(p1)
        parent2 = find(p2)

        if parent1 < parent2:
            parent[parent2] = parent1
        else:
            parent[parent1] = parent2
    
    # main
    for p1, p2 in points:
        if find(p1) == find(p2):
            return turn
        union(p1, p2)

        turn += 1

    return 0


if __name__ == "__main__":
    print(solution(*read_data()))
