# 백준 #17425 약수의 합
'''
    Algorithm: math, 누적합
    Time Complexity: O(NlnN)

'''
import sys
from typing import Callable, NoReturn


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def solution() -> NoReturn:
    MAX_NUM = 1000001

    f = [i for i in range(MAX_NUM)]
    g = [0 for _ in range(MAX_NUM)]

    for i in range(1, MAX_NUM):
        for j in range(2*i, MAX_NUM, i):
            f[j] += i
        
    g[1] = f[1]

    for i in range(2, MAX_NUM):
        g[i] = g[i-1] + f[i]

    T = int(input())

    for _ in range(T):
        N = int(input())
        print(g[N])


if __name__ == "__main__":
    solution()
