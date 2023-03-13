# 백준 #16120 PPAP
'''
    Algorithm: 스택
    Time Complexity: O(N)
'''
import sys
from typing import Tuple, Callable

PPAP = ['P', 'P', 'A', 'P']

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    S = input()
    return S,


def solution(S:str) -> int:
    stack = []

    for s in S:
        stack.append(s)

        while stack[-4:] == PPAP:
            for _ in range(3):
                stack.pop()

    if stack == ['P']:
        return 'PPAP'

    return 'NP'


if __name__ == "__main__":
    print(solution(*read_data()))
