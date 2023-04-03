# 백준 #12904 A와 B
'''
    Algorithm: 구현
    Time Complexity: O(T^2)

'''
import sys
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    S = list(input())
    T = list(input())
    return S, T


def solution(S:str, T:List[str]) -> int:

    while len(S) < len(T):
        if T.pop() == 'B':
            T.reverse()
        
    return int(S == T)


if __name__ == "__main__":
    print(solution(*read_data()))
