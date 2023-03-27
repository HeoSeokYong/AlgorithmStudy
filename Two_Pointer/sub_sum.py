# 백준 #1806 부분합
'''
    Algorithm: 투 포인터
    Time Complexity: O(N)

'''
import sys
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, S = map(int, input().split())
    nums = list(map(int, input().split()))
    return N, S, nums


def solution(N:int, S:int, nums:List[int]) -> int:
    result = N + 1
    l, r = 0, 1
    sub_sum = nums[0]
    
    while l < N:
        if r < N and sub_sum < S:
            sub_sum += nums[r]
            r += 1
        else:
            if sub_sum >= S:
                result = min(result, r - l)
            sub_sum -= nums[l]
            l += 1

    return result if result != N + 1 else 0


if __name__ == "__main__":
    print(solution(*read_data()))
