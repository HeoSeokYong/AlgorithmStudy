# 백준 #2448 별 찍기 - 11
'''
    Algorithm: 재귀
    Time Complexity: -

    N은 별들의 높이
'''
import sys
from typing import Tuple, Callable

STAR = ["  *  ", " * * ", "*****"]
BLANK = " "

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    return N,


def solution(N:int) -> str:
    def counting_star(x:int):
        if x == 3:
            return STAR
        
        stars = []
        c_stars = counting_star(x//2)

        # 기존 트리를 가운데로 옮김
        for s in c_stars:
            stars.append(BLANK * (x//2) + s + BLANK * (x//2))

        # 기존 트리를 아래에 2개 붙인다.
        for s in c_stars:
            stars.append(s + BLANK + s)

        return stars

    return "\n".join(counting_star(N))


if __name__ == "__main__":
    print(solution(*read_data()))
