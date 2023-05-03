# 백준 #17612 쇼핑몰
'''
    Algorithm: 우선순위큐
    Time Complexity: O(NlogN)
'''
import sys
import heapq
from typing import Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, k = map(int, input().split())
    return N, k


def solution(N:int, k:int) -> int:
    heap = []
    counters = [(0, i) for i in range(k)]

    for _ in range(N):
        id, w = map(int, input().split())

        waiting_time, guide_idx = heapq.heappop(counters)

        heapq.heappush(counters, (waiting_time + w, guide_idx))
        heapq.heappush(heap, (waiting_time + w, -guide_idx, id))

    del counters

    return sum(heapq.heappop(heap)[2] * i for i in range(1, N+1))


if __name__ == "__main__":
    print(solution(*read_data()))