# 백준 #1368 물대기
'''
    Algorithm: MST - kruskal
    Time Complexity: O(N^2logN)

'''
import sys

from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    costs = []
    
    for i in range(1, N+1):
        costs.append((int(input()), 0, i))
    
    for i in range(1, N+1):
        it = iter(map(int, input().split()))
        for j in range(1, N+1):
            if i == j:
                next(it)
                continue

            costs.append((next(it), i, j))

    return N, costs


def solution(N:int, costs:List[int]) -> int:
    result = 0
    parents = [i for i in range(N+1)]

    def find_parent(x:int) -> int:
        if parents[x] != x:
            parents[x] = find_parent(parents[x])
        return parents[x]
    
    def union_parent(x:int, y:int):
        x = find_parent(x)
        y = find_parent(y)

        if x == y:
            return False
        else:
            parents[y] = x
            return True

    for cost, a, b in sorted(costs):
        if union_parent(a, b):
            result += cost

    return result


if __name__ == "__main__":
    print(solution(*read_data()))
