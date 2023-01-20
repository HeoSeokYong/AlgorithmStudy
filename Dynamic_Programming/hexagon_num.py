# 백준 #1229 육각수
'''
    Algorithm: dp
    Time Complexity: O(NH) (H: 육각수 배열의 길이)

    육각수  h_n = h_{n-1} + (n-1)*4 + 1  (n=1, h_n = 1)

    dp[i][j] = 육각수를 i번 골랐을 때의 합 
		Python3 시간초과. PyPy3 정답.
'''
import sys
import math
from typing import Tuple, Callable

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    return N,


def solution(N: int) -> int:
    def get_hexa_num(n):
        ''' n보다 같거나 작은 육각수들의 배열을 반환 '''
        hexa = [1]
        while (x := hexa[-1] + 4*(len(hexa)) + 1) <= n:
            hexa.append(x)

        return hexa
    
    INF = 10 ** 8
    h = get_hexa_num(N)
    dp = [INF for _ in range(N+1)]

    for i in range(len(h)):
        dp[h[i]] = 1

    for i in range(1, 6):
        if dp[N] != INF:
            break
        for j in range(N):
            if dp[j] == i:
                for k in range(len(h)):
                    if j + h[k] <= N:
                        dp[j + h[k]] = min(dp[j + h[k]], dp[j] + 1)

    return dp[N]


if __name__ == "__main__":
    print(solution(*read_data()))