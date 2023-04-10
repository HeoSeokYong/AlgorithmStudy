# 백준 #1083 소트
'''
    Algorithm: greedy
    Time Complexity: O(SN^3)

'''
import sys
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    A = list(map(int, input().split()))
    S = int(input())
    return N, A, S


def solution(N:int, A:List[int], S:int) -> List[int]:
    idx = 0

    while S > 0 and idx < N:
        max_idx = A.index(max(A[idx:idx+S+1]))
        
        if max_idx > idx:
            S -= (max_idx-idx)
            A.insert(idx, A.pop(max_idx))
        else:
            idx += 1

    return A


if __name__ == "__main__":
    print(*solution(*read_data()))
