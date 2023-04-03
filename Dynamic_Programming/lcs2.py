# 백준 #9252 LCS 2
'''
    Algorithm: dp
    Time Complexity: O(l1*l2)

'''
import sys
from typing import Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    s1 = input()
    s2 = input()
    return s1, s2


def solution(s1:str, s2:str) -> int:
    l1, l2 = len(s1), len(s2)

    dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]

    for i in range(l1):
        for j in range(l2):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    len_lcs = dp[-1][-1]

    print(len_lcs)

    res = ["" for _ in range(len_lcs)]
    
    while l1 > 0 and l2 > 0:
        if dp[l1][l2] == dp[l1][l2-1]:
            l2 -= 1
        elif dp[l1][l2] == dp[l1-1][l2]:
            l1 -= 1
        else:
            res[len_lcs-1] = s1[l1-1]
            len_lcs -= 1
            l1 -= 1
            l2 -= 1


    print("".join(res))

if __name__ == "__main__":
    solution(*read_data())
