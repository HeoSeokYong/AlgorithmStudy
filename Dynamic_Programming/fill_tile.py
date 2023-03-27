# 백준 #2133 타일 채우기
'''
    Algorithm: dp
    Time Complexity: O(N)

    3 X N 크기의 벽을 1x2, 2x1 크기의 타일로 채우는 경우의 수

    N = 홀수 -> 안됨
    - N = 짝수
    N = 2, 경우의 수 3
    N = 4, N=2인 경우의 수 * N=2인 경우의 수 + 두 타일을 붙였을 때 나오는 새로운 경우의 수(=2)
    N인 블록을 크기가 짝수인 블록으로 나눈다.
    N : (N-2, 2), (N-4, 4), ..., (2, N-2)
    두 타일이 연결된 경우를 제외하고 do[N-2] * dp[2]로 총 경우의 수를 구한다.
    여기에 두 타일을 붙이는 경우의 수들을 더해준다.
    (N-2, 2) => 2
    (N-4, 4) => dp[N-4] * 2 : 크기 N-4의 타일을 정하는 경우의 수 + 크기가 N-4와 4인 타일을 붙이는 경우의 수(=2)
    ... 
    (2, N-2) => dp[2] * 2

'''
import sys
from typing import Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    return N,


def solution(N:int) -> int:
    dp = [0 for _ in range(N+2)]
    dp[0], dp[2] = 1, 3
    prev_sum = dp[0]

    for i in range(2, N - 1, 2):
        dp[i + 2] = dp[2] * dp[i] + prev_sum * 2
        prev_sum += dp[i]

    return dp[N]


if __name__ == "__main__":
    print(solution(*read_data()))
