# 백준 #2230 수 고르기 https://www.acmicpc.net/problem/2230
'''
    Algorithm: 투 포인터
    Time Complexity: O(NlogN)

    수열 A를 정렬한 후 투 포인터를 활용해 차이가 적을 때를 찾아보자.
    l과 r의 차이가 M보다 작을 경우 r을 크게 하고,
    M보다 커질 경우 l을 크게 한다.
'''
import sys
from typing import List, Tuple, Callable

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    return N, M, A


def solution(N: int, M: int, A: List[int]) -> int:
    result = float('inf')
    l, r = 0, 0
    A.sort()

    while r < N:
        if l == r or A[r] - A[l] < M:     
            r += 1
        else:
            result = min(result, A[r] - A[l])
            l += 1

    return result


if __name__ == "__main__":
    print(solution(*read_data()))

