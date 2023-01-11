# 백준 #11049 행렬 곱셈 순서
'''
    Algorithm: dp
    Time Complexity: O(N^3)

    dp[i][j] : i~j번째 행렬까지의 곱의 최솟값
        - 대각선방향으로 업데이트 
        i~k의 합 + k+1~j의 합 + i~j까지의 연산량
    
    => pypy3 통과. python3 시간초과.
'''
import sys
from typing import List, Tuple

input = sys.stdin.readline

def solution(N:int, matrix: List[Tuple]) -> int:
    dp = [[0 for _ in range(N)] for _ in range(N)]

    for j in range(1, N):
        for i in range(N-j):
            dp[i][i+j] = min([dp[i][k] + dp[k+1][i+j] + (matrix[i][0] * matrix[k][1] * matrix[i+j][1]) for k in range(i, i+j)])

    return dp[0][N-1]


if __name__ == "__main__":
    N = int(input())
    matrix = [tuple(map(int, input().split())) for _ in range(N)]

    print(solution(N, matrix))

# ---------------------------------------
'''
    Algorithm: dp
    Time Complexity: O(N^3)

    python3 통과, 문제 풀이는 위와 같고 컴파일 타임을 줄일 여러 기법을 적용.
'''
import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    matrix = [x for x, _ in matrix] + [matrix[-1][1]]
    dp = [[0 for _ in range(N)] for _ in range(N)]

    for d in range(1, N):
        for i in range(N-d):
            j = i+d

            tmp = min(ik + (matrix[i]*k*matrix[j+1]) + kj for ik, k, kj in zip(dp[i][i:j], matrix[i+1:j+1], dp[j][i+1:j+1]))
            dp[i][j] = dp[j][i] = tmp

    print(dp[0][N-1])

solution()