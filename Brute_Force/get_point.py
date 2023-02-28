# 백준 #1749 점수따먹기
'''
    Algorithm: 누적 합, 브루트포스
    Time Complexity: O((NM)^2)

    누적합을 통해 모든 부분 행렬의 합을 조사한다.
'''
import sys
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    return N, M, matrix


def solution(N:int, M:int, matrix:List[List[int]]) -> int:
    # 누적 합
    prefix_sum = [[0 for _ in range(M+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, M+1):
            prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + matrix[i-1][j-1]

    result = matrix[0][0]

    # 부분 행렬 (rs~re, cs~ce) 
    for rs in range(1, N+1):
        for cs in range(1, M+1):
            for re in range(rs, N+1):
                for ce in range(cs, M+1):
                    result = max(result, prefix_sum[re][ce] - prefix_sum[rs-1][ce] - prefix_sum[re][cs-1] + prefix_sum[rs-1][cs-1])

    return result


if __name__ == "__main__":
    print(solution(*read_data()))
