# 백준 #2467 용액
'''
    Algorithm: 투 포인터
    Time Complexity: O(N)

'''
import sys
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    sols = list(map(int, input().split()))
    return N, sols


def solution(N:int, sols:List[int]) -> Tuple:
    result = float('inf')
    l, r = 0, N-1

    while l < r:
        if result > abs(sols[l] + sols[r]):
            result = abs(sols[l] + sols[r])
            ret = (sols[l], sols[r])

        if sols[l] + sols[r] < 0:
            l += 1
        else:
            r -= 1

    return ret


if __name__ == "__main__":
    print(*solution(*read_data()))
