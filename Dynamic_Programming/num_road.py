# 백준 #1577 도로의 개수
'''
    Algorithm: dp
    Time Complexity: O(NM)

    (0, 0) -> (N, M) 까지최단 경로로만 가기 때문에 
    x y가 증가하는 방향으로만 이동하게 된다.
'''
import sys
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, M = map(int, input().split())
    K = int(input())
    # construction: [내려가는 경우, 오른쪽으로 가는 경우]
    construction = [[[True, True] for _ in range(M+1)] for _ in range(N+1)]

    for _ in range(K):
        a, b, c, d = map(int, input().split())
        a, b, c, d = (a, b, c, d) if a < c or b < d else (c, d, a, b)
        construction[a][b][a == c] = False

    return N, M, construction


def solution(N:int, M:int, construction:List) -> int:
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

    for i in range(N+1):                 
        for j in range(M+1):
            if i == 0 and j == 0:
                dp[i][j] = 1
            else:
                if i > 0 and construction[i-1][j][0]:
                    dp[i][j] += dp[i-1][j]

                if j > 0 and construction[i][j-1][1]:
                    dp[i][j] += dp[i][j-1]

    return dp[N][M]


if __name__ == "__main__":
    print(solution(*read_data()))