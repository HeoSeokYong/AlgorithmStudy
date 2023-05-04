# 백준 #12892 생일 선물
'''
    Algorithm: two pointer
    Time Complexity: O(NlogN)
'''
import sys

from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, D = map(int, input().split())
    presents = [tuple(map(int, input().split())) for _ in range(N)]
    return N, D, presents


def solution(N:int, D:int, presents:List[Tuple]) -> int:
    result = 0

    presents.sort() 
    
    s, e = 0, 0
    satisfaction = 0
    
    while e < N:
        scost, slev = presents[s]
        ecost, elev = presents[e]

        if ecost - scost >= D:
            satisfaction -= slev
            s += 1
        else:
            satisfaction += elev
            e += 1

            result = max(result, satisfaction)

    return result


if __name__ == "__main__":
    print(solution(*read_data()))
