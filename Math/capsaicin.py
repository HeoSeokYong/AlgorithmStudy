# 백준 #15824 너 봄에는 캡사이신이 맛있단다
'''
    Algorithm: 수학
    Time Complexity: O(NlogN)

    try 1)
        1 2 3 4 5

        큰 값부터 자기 이전 수의 개수를 n이라 할때, nC1 만큼 들어감(+)
        작은 값은 자기 이후의 수를 n이라 할때, nC1 만큼 들어감(-)
        [1 2] [1 3] [1 4] [1 5] [2 3] [2 4] [2 5] [3 4] [3 5] [4 5]

        마찬가지, nC2
        [1 2 3] [1 2 4] [1 2 5] [1 3 4] [1 3 5] [1 4 5]
        [2 3 4] [2 3 5] [2 4 5] [3 4 5]

        -> 총개수 -1 까지 진행 : 결국 N^2이 되어 시간이 초과된다.

    try 2)
        두 수 a, b (a<=b)에 대해 a와 b 사이의 원소의 개수를 k라고 할 때
        최솟값이 a이고 최댓값이 b인 조합의 개수는 2^k 라고 한다.

        ex) [1, 2, 3, 4]
        k=0 ) [1,2] [2,3] [3,4] => 2-1 + 3-2 + 4-3 
                                = 2+3+4 - (1+2+3) 이 2^k개 있는 것이다. 
        k=1 ) 3+4 - (1+2)
        k=2 ) 4 - 1

'''
import sys
from typing import List, Tuple, Callable

MOD = 1000000007

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    scoville_scale = list(map(int, input().split()))
    return N, scoville_scale


def solution(N:int, scoville_scale:List[int]) -> int:
    result = 0

    scoville_scale.sort()
    max_spicy, min_spicy = 0, 0

    for k in range(N//2):
        max_spicy = (max_spicy + scoville_scale[-1-k]) % MOD
        min_spicy = (min_spicy + scoville_scale[k]) % MOD

        result += (max_spicy - min_spicy) * (pow(2, N-2-k) + pow(2, k)) % MOD

    if N % 2 == 0: # even
        result -= (max_spicy - min_spicy) * pow(2, k) % MOD

    return result % MOD


if __name__ == "__main__":
    print(solution(*read_data()))