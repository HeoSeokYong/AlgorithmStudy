# 백준 #2866 문자열 잘라내기
'''
    Algorithm: 이분탐색
    Time Complexity: O(RClogR)

'''
import sys
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    R, C = map(int, input().split())
    table = [input() for _ in range(R)]
    return R, C, table


def solution(R:int, C:int, table:List[str]) -> int:
    result = 0
    start, end = 0, R

    while start < end:
        mid = (start + end) >> 1
        
        check = set()
        flag = False

        for j in range(C):
            s = "".join(table[i][j] for i in range(mid, R))
            
            if s not in check:
                check.add(s)
            else:
                flag = True
                break
        
        if flag:
            end = mid
        else:
            start = mid+1
            result = mid


    return result


if __name__ == "__main__":
    print(solution(*read_data()))
