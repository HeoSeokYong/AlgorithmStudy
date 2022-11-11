# 백준 #1520 내리막 길
'''
    Algorithm: DP
    Time Complexity:

'''
import sys

input = sys.stdin.readline
dxdy = ((0, 1), (1, 0), (0, -1), (-1, 0))

def solution(M, N):
    maps = [list(map(int, input().split())) for _ in range(M)]
    dp = [[0] * N for _ in range(M)]

    for i in range(M):
        for j in range(N):
            if i == 0 and j == 0:
                dp[i][j] = 1
            else:
                for di, dj in dxdy:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < M and 0 <= nj < N and maps[i][j] > maps[ni][nj]:
                        dp[ni][nj] += 1

    for d in dp:
        print(d)

    return


if __name__ == "__main__":
    M, N = map(int, input().split())

    print(solution(M, N))