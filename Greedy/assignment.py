# 백준 #13904 과제
'''
    Algorithm: greedy, heapq
    Time Complexity: O(NlogN)

    하루에 과제 하나
    마지막 날부터 탐색하자.
'''
import sys
import heapq
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    assignments = [tuple(map(int, input().split())) for _ in range(N)]
    return N, assignments


def solution(N:int, assignments:List[Tuple]) -> int:
    result = 0
    assignments.sort()
    day = assignments[-1][0]
    heap = []

    while day > 0:
        while assignments and assignments[-1][0] == day:
            d, w = assignments.pop()
            heapq.heappush(heap, -w)
        if heap:
            result -= heapq.heappop(heap)

        day -= 1

    return result


if __name__ == "__main__":
    print(solution(*read_data()))
