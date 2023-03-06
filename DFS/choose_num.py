# 백준 #2668 숫자고르기
'''
    Algorithm: dfs
    Time Complexity: O(NlogN)

'''
import sys
from typing import Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    return N,


def solution(N:int) -> int:
    result = []
    path = [0 for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]

    def dfs(x:int):
        stack = [x]
        visited[x] = x # x로부터 시작된 집합들

        while stack:
            nxt = path[stack[-1]]

            if not visited[nxt]:
                stack.append(nxt)
                visited[nxt] = x
            else:
                if visited[nxt] == x:
                    while True:
                        num = stack.pop()
                        result.append(num)

                        if num == nxt:
                            break
                return
            
    # main
    for i in range(1, N+1):
        path[i] = int(input())

    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)

    return [len(result)] + sorted(result)


if __name__ == "__main__":
    print(*solution(*read_data()), sep='\n')
