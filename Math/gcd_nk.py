# 백준 #11689 GCD(n, k) = 1
'''
    Algorithm: 수학, 정수론, 오일러-파이 함수
    Time Complexity: O(sqrt(N) + logN)

    오일러-파이 함수(N): 1부터 N까지 중 N과 서로소인 수의 개수
    N보다 작은 소수들의 집합 중 N에 소인수에 들어가는 원소들을
    오일러-파이 함수 식에 넣어 계산한다.
'''
import sys
from typing import Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    return N, 


def solution(N:int) -> int:
    result = N
    factors = set()
    p = 2

    while p*p <= N:
        if N % p == 0:
            N //= p
            factors.add(p)
        else:
            p += 1

    if N > 1:
        factors.add(N)

    for factor in factors:
        result *= (factor - 1) / factor

    return int(result)


if __name__ == "__main__":
    print(solution(*read_data()))
