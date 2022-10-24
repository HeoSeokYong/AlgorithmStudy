# 백준 #1103 게임
'''
    Algorithm: dfs, dp
    Time Complexity: O(NM) ?  잘모르겠다.
    dp와 visited를 분리시켜서 해보자.
    dp: 해당 지점까지 가는 최대 회수
'''
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def solution(N, M, board):
    answer = 0
    dxdy = ((0, -1), (-1, 0), (1, 0), (0, 1))

    dp = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    def dfs(d, x, y):
        nonlocal answer
        if answer == -1:
            return
        else:
            answer = max(answer, d)

        num = int(board[x][y])

        for dx, dy in dxdy:
            dx, dy = dx*num, dy*num
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 'H' and d+1 > dp[nx][ny]:
                if visited[nx][ny]:
                    answer = -1
                    return
                dp[nx][ny] = d+1
                visited[nx][ny] = True
                dfs(d+1, nx, ny)
                visited[nx][ny] = False

    visited[0][0] = True
    dfs(1, 0, 0)

    return answer


if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]

    print(solution(N, M, board))