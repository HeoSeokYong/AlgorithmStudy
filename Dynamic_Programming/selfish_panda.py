# 백준 #1937 욕심쟁이 판다
'''
    Algorithm: dp
    Time Complexity: O(N^2logN^2)

    heap을 써서 최소 대나무부터 주변의 많은 대나무가 있는 곳에 dp +1
'''
import sys
import heapq

input = sys.stdin.readline

def solution(N: int) -> int:
    answer = 1
    dxdy = ((0, 1), (1, 0), (0, -1), (-1, 0))

    forest = [list(map(int, input().split())) for _ in range(N)]
    dp = [[1] * N for _ in range(N)]

    heap = []
    for i in range(N):
        for j in range(N):
            heapq.heappush(heap, (forest[i][j], i, j))

    while heap:
        b, x, y = heapq.heappop(heap)

        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and b < forest[nx][ny] and dp[nx][ny] < dp[x][y] + 1:
                dp[nx][ny] = dp[x][y] + 1
                answer = max(answer, dp[nx][ny])

    return answer


if __name__ == "__main__":
    N = int(input())

    print(solution(N))