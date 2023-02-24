# 백준 #13269 쌓기나무
'''
    Algorithm: greedy
    Time Complexity: O(NM)

'''
import sys
from typing import List, Tuple, Callable

INF = sys.maxsize

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, M = map(int, input().split())
    view = [list(map(int, input().split())) for _ in range(N+2)]
    return N, M, view


def solution(N:int, M:int, view:List[List[int]]) -> List[List[int]]:
    right_view = view.pop()
    front_view = view.pop()
    result = [[INF if view[i][j] else 0 for j in range(M)] for i in range(N)]

    for i in range(N):
        for j in range(M):
            if result[i][j]:
                result[i][j] = min(result[i][j], front_view[j])
                result[i][j] = min(result[i][j], right_view[N-1-i])
    
    # right check
    for i in range(N):
        if max(result[i]) < right_view[N-1-i]:
            return [-1]
    
    # front check
    for j in range(M):
        if max(result[i][j] for i in range(N)) < front_view[j]:
            return [-1]

    return [" ".join(map(str, r)) for r in result]


if __name__ == "__main__":
    print(*solution(*read_data()), sep='\n')
