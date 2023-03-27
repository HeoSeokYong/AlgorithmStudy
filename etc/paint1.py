# 백준 #1117 색칠 1
'''
    Algorithm: 구현
    Time Complexity: O(1)

'''
import sys
from typing import Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    W, H, f, c, x1, y1, x2, y2 = map(int, input().split())
    return W, H, f, c, x1, y1, x2, y2


def solution(W:int, H:int, f:int, c:int, x1:int, y1:int, x2:int, y2:int) -> int:
    f = min(W - f, f)

    if f <= x1:
        area = x2 - x1
    elif x2 <= f:
        area = (x2 - x1) * 2
    else: # x1 < f < x2
        area = (f-x1) * 2 + x2 - f
    
    area *= (y2-y1) * (c+1)

    return W*H - area


if __name__ == "__main__":
    print(solution(*read_data()))
