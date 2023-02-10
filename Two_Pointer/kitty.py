# 백준 #16472 고냥이
'''
    Algorithm: 투포인터
    Time Complexity: O(N)
'''
import sys
from typing import Tuple, Callable
from collections import defaultdict


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    meow = str(input())
    return N, meow


def solution(N:int, meow:str) -> int:
    result = 0
    l, r = 0, 0
    translator = defaultdict(int)

    while r < len(meow):
        if len(translator) < N:
            translator[meow[r]] += 1
            r += 1
        else:
            if meow[r] not in translator:
                while tm := translator[meow[l]] - 1:
                    translator[meow[l]] = tm
                    l += 1

                translator.pop(meow[l])
                l += 1

            translator[meow[r]] += 1
            r += 1

        result = max(result, r-l)

    return result



if __name__ == "__main__":
    print(solution(*read_data()))