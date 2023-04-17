# 백준 #7570 줄 세우기
'''
    Algorithm: dp
    Time Complexity: O(N)

    dp[i] : i번째 아이가 맨 뒤로 가기위해 필요한 이동수 = i-1번째가 맨 뒤로 가기 위한 이동 수 + 1
'''
import sys
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    kids = list(map(int, input().split()))
    return N, kids


def solution(N:int, kids:List[int]) -> int:
    dp = [0 for _ in range(N+1)]

    for i in range(N):
        dp[kids[i]] = dp[kids[i]-1] + 1

    return N - max(dp)


if __name__ == "__main__":
    print(solution(*read_data()))
