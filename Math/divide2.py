# 백준 #1407 2로 몇 번 나누어질까까
'''
    Algorithm: 재귀, 수학
    Time Complexity: O(logB)

    1부터 시작하여 2의 거듭제곱 꼴인 최대의 약수를 기록하면 일정한 순서가 보인다.
    1 2 1 4 1 2 1 8 
    1 2 1 4 1 2 1 16 
    1 2 1 4 1 2 1 8 
    1 2 1 4 1 2 1 32
    1 2 1 4 1 2 1 8 
    1 2 1 4 1 2 1 16
    1 2 1 4 1 2 1 8
    1 2 1 4 1 2 1 64

    f(x)
    f(odd) => 1
    f(even) => f(x//2) * 2
    - 구간 합
    x가 짝수면 1~x까지 2의 약수의 합 중 절반은 1이다. -> x // 2
    나머지는 짝수다. => 2*f(x//2)
    x가 홀수면 자신까지 + 1
'''
import sys
from typing import Tuple, Callable

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    A, B = map(int, input().split())
    return A, B 


def solution(A: int, B: int) -> int:
    def f(x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        elif x % 2:
            return x // 2 + 2*f(x//2) + 1
        else:
            return x // 2 + 2*f(x//2)

    return f(B) - f(A-1)


if __name__ == "__main__":
    print(solution(*read_data()))

