# 백분 #1915 가장 큰 정사각형
'''
    Algotirhm: dp
    Time Complexity: O(N*M)
'''
import sys

input = sys.stdin.readline

def solution(N, M):
    answer = 0
    arr = [[int(x) for x in input().rstrip()] for _ in range(N)]
    dp = [[0] * M for _ in range(N)]

    for i in range(N):
        if arr[i][0] == 1:
            dp[i][0] = 1
            answer = 1
    
    for j in range(M):
        if arr[0][j] == 1:
            dp[0][j] = 1
            answer = 1

    for i in range(1, N):
        for j in range(1, M):
            if arr[i][j] == 1:
                dp[i][j] = min((dp[i-1][j], dp[i][j-1], dp[i-1][j-1])) + 1
                answer = max(answer, dp[i][j])

    return answer ** 2


if __name__ == "__main__":
    N, M = map(int, input().split())

    print(solution(N, M))