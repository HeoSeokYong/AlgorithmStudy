# 백준 #17471 게리맨더링
'''
    Algorithm: brute-force, bfs
    Time Complexity: -

'''
import sys
from typing import Set, List, Tuple, Callable
from itertools import combinations
from collections import deque


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    population = [0] + list(map(int, input().split()))
    path = [[] for _ in range(N+1)]

    for i in range(1, N+1):
        adjs = list(map(int, input().split()))
        path[i] = adjs[1:]

    return N, population, path


def solution(N:int, population:List[int], path:List[List[int]]) -> int:
    MAXPOP = sum(population)
    result = MAXPOP
    city = set(range(1, N+1))

    def check(comb:Tuple) -> bool:
        area1 = set(comb)
        area2 = city - area1
        visited = [True] + [False for _ in range(N)]

        def bfs(area:Set):
            q = deque([list(area)[0]])
            visited[q[0]] = True

            while q:
                x = q.popleft()

                for nx in path[x]:
                    if not visited[nx] and nx in area:
                        visited[nx] = True
                        q.append(nx)

        bfs(area1)
        bfs(area2)
        
        if all(visited):
            return True
        
        return False

    for k in range(1, N):
        for comb in combinations(city, k):

            if check(comb):
                pts = 0
                for i in range(1, N+1):
                    if i in comb:
                        pts += population[i]
                    else:
                        pts -= population[i]

                result = min(result, abs(pts))

    if result == MAXPOP:
        return -1
    
    return result


if __name__ == "__main__":
    print(solution(*read_data()))
