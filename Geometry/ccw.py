# 백준 #11758 CCW
'''
    Algorithm: CCW
    Time Complexity: O(1)

'''
import sys
from typing import Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    points = [tuple(map(int, input().split())) for _ in range(3)]
    return points


def solution(p1: Tuple, p2: Tuple, p3:Tuple) -> int:

    def CCW(p1: Tuple, p2: Tuple, p3:Tuple) -> int:
        S = p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] \
            - (p1[0]*p3[1] + p2[0]*p1[1] + p3[0]*p2[1])
        
        if S > 0:
            return 1
        elif S < 0:
            return -1
        else:
            return 0
    
    def CCW2(p1: Tuple, p2: Tuple, p3:Tuple) -> int:
        ''' 2023.03.02 풀이 '''
        S = (p2[0] - p1[0])*(p3[1] - p1[1]) - (p3[0] - p1[0])*(p2[1] - p1[1])

        if S > 0:
            return 1
        elif S < 0:
            return -1
        else:
            return 0
        
    return CCW2(p1, p2, p3)


if __name__ == "__main__":
    print(solution(*read_data()))