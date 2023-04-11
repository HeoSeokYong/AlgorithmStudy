# 백준 #9935 문자열 폭발
'''
    Algorithm: stack
    Time Complexity: O(NM)

'''
import sys
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    S = list(input())
    bomb = input()
    return S, bomb


def solution(S:List[str], bomb:str) -> str:
    N, M = len(S), len(bomb)
    stack = []

    for s in S:
        stack.append(s)
        if s == bomb[-1] and "".join(stack[-M:]) == bomb:
            del stack[-M:]

    return "".join(stack) if stack else "FRULA"


if __name__ == "__main__":
    print(solution(*read_data()))
