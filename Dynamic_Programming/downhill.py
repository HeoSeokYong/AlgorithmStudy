# 백준 #1520 내리막 길
'''
    Algorithm: DP, dfs
    Time Complexity: -

    dfs로 탐색을 하며 dp에 정보를 기록해 중복 탐지를 방지.
'''
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
dxdy = ((0, 1), (1, 0), (0, -1), (-1, 0))

def solution(M, N):
    maps = [list(map(int, input().split())) for _ in range(M)]
    dp = [[-1] * N for _ in range(M)]

    def dfs(x, y):
        if x == M-1 and y == N-1:
            return 1
        
        if dp[x][y] == -1:
            dp[x][y] = 0
            for dx, dy in dxdy:
                nx, ny = x + dx, y + dy
                if 0 <= nx < M and 0 <= ny < N and maps[x][y] > maps[nx][ny]:
                    dp[x][y] += dfs(nx, ny)

        return dp[x][y]

    return dfs(0, 0)


if __name__ == "__main__":
    M, N = map(int, input().split())

    print(solution(M, N))