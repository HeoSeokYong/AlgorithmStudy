# 백준 #16565 N포커
'''
    Algorithm: dp, 수학
    Time Complexity: O(C^2) (C: 트럼프 카드의 개수=52)

    n_C_k = n-1_C_k-1 + n-1_C_k 이 공식을 사용해서
    미리 53범위의 combination 값들을 저장해놓는다.
    => N의 크기가 크지 않아 math.comb로 해도 가능하다.

    플레이어가 이기는 경우는 포카드가 1개 이상 있을 경우이다.
    이후 N개 중 포카드를 x세트 뽑는 경우의 수와 나머지 중 N-4x 개의 카드를 뽑는 경우의 수를 곱해주면 되겠다.

    포카드 1개와 나머지를 뽑는 경우의 수 안에 포카드 2개 이상이 들어있는 경우가 있다.
    => 포함 배제의 원리를 통해 합집합의 개수를 구할 수 있다.

'''
import sys
from typing import Tuple, Callable

MOD = 10007

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    return N, 


def solution(N:int) -> int:
    result = 0
    combs = [[0 for _ in range(53)] for _ in range(53)]

    for i in range(53):
        combs[i][0] = combs[i][i] = 1
        for j in range(1, i):
            combs[i][j] = (combs[i-1][j-1] + combs[i-1][j]) % MOD
            combs[i][i-j] = combs[i][j]
    
    for x in range(4, N+1, 4):
        if (x//4) % 2:
            result += combs[13][x//4] * combs[52-x][N-x]
        else:
            result -= combs[13][x//4] * combs[52-x][N-x]

        result %= MOD

    return result


if __name__ == "__main__":
    print(solution(*read_data()))
