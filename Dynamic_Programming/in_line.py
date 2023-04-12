# 백준 #2631 줄세우기
'''
    Algorithm: dynamic programming(LIS)
    Time Complexity: O(N^2)

    오름차순 정렬해야 함.
    => 이미 오름차순인 애들은 옮길 필요없음.
    => LIS 찾기
'''
import sys
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    kids = [int(input()) for _ in range(N)]
    return N, kids


def solution(N:int, kids:List[int]) -> int:
    dp = [1 for _ in range(N)]

    for i in range(N):
        for j in range(i):
            if kids[j] < kids[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return N - max(dp)


if __name__ == "__main__":
    print(solution(*read_data()))
