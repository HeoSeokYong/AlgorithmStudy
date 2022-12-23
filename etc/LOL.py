# 백준 #23327 리그전 오브 레전드
'''
    Algorithm: 누적합
    Time Complexity: O(N+Q)

    누적합, 누적 그룹 재미합

    ex) 5 1 2 3 2
        [3, 5] : 2, 3, 2 => 16

        [5, 6, 8, 11, 13] : prefix (누적합)
        [0, 5, 17, 41, 63] : prefun (누적 그룹 재미합)

        prefun[5] - prefun[2]
        (위치)
        1*2 1*3 1*4 1*5 2*3 2*4 2*5 3*4 3*5 4*5 - 1*2
        답인 3*4 3*5 4*5 를 뺀 나머지를 더 빼줘야 함.
        1*3 1*4 1*5 2*3 2*4 2*5 = (3+4+5)*(1+2)
        = (prefix[5]-prefix[2])*prefix[2]

        => l, r의 경우
        answer = prefun[r] - prefun[l-1] - (prefix[r]-prefix[l-1])*prefix[l-1]
'''
import sys
from typing import List

input = sys.stdin.readline

def solution(N: int, Q: int, popularity: List[int]) -> None:
    prefix = [0] + popularity[:]
    prefix_fun = [0 for _ in range(N+1)]

    for i in range(1, N):
        prefix[i+1] = prefix[i] + popularity[i]
        prefix_fun[i+1] = prefix_fun[i] + popularity[i] * prefix[i]

    for _ in range(Q):
        l, r = map(int, input().split())

        print(prefix_fun[r] - prefix_fun[l-1] - (prefix[r]-prefix[l-1])*prefix[l-1])


if __name__ == "__main__":
    N, Q = map(int, input().split())
    popularity = list(map(int, input().split()))

    solution(N, Q, popularity)