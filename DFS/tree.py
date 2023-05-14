# 백준 #1068 트리
'''
    Algorithm: dfs, tree
    Time Complexity: O(N)

'''
import sys

from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    parents = list(map(int, input().split()))
    del_node = int(input())
    return N, parents, del_node


def solution(N:int, parents:List[int], del_node:int) -> int:
    result = 0
    stack = []
    tree = [[] for _ in range(N)]

    for i in range(N):
        if parents[i] == -1:
            stack.append(i)
        elif i != del_node:
            tree[parents[i]].append(i)

    while stack:
        node = stack.pop()

        if node == del_node:
            continue

        if not tree[node]:
            result += 1

        for n in tree[node]:
            stack.append(n)

    return result


if __name__ == "__main__":
    print(solution(*read_data()))
