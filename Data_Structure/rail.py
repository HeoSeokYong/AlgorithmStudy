# 백준 # 13334 철로
'''
    Algorithm: 정렬, 우선순위큐
    Time Complexity: O(NlogN)

    try 1)
    시작지점 기준 정렬 + 큐
    -> 시작지점이 늦더라도 범위가 작아 포함되는 경우를 찾지 못한다.

    try 2)
    그러면 뒷 지점을 기준으로 정렬해보자.
    d보다 큰 구간은 제외하고 진행한다.

    큐가 안된다.
    - 들어올 때는 도착 지점 기준 정렬이지만
    나갈 때는 출발 지점 기준이어야 해서 큐는 안된다.
    => 힙을 쓰자.
'''
import sys
import heapq
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    path = [tuple(map(int, input().split())) for _ in range(N)]
    d = int(input())
    return N, path, d


def solution(N:int, path:List[Tuple], d:int) -> int:
    result = 0
    heap = []

    for h, o in sorted(path, key= lambda x: max(x)):
        if abs(h - o) <= d:
            heapq.heappush(heap, (h, o) if h <= o else (o, h))

            # 현재 들어간 경로의 도착지점부터 범위를 비교
            while heap and heap[0][0] < max(h, o) - d:
                heapq.heappop(heap)
                heapq.h
            
            result = max(result, len(heap))
            
    return result


if __name__ == "__main__":
    print(solution(*read_data()))