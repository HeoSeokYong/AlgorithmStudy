import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())
world = [list(map(int, input().split())) for i in range(N)]

visited = [[False] * N for _ in range(N)]
num_island = 1
minDist = INF

def island(i, j, num_island):
    q = deque([(i, j)])
    visited[i][j] = True
    world[i][j] = num_island

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N \
            and visited[nx][ny] == False \
            and world[nx][ny] == 1:
                visited[nx][ny] = True
                world[nx][ny] = num_island
                q.append((nx, ny))

def find_bridge(k):
    q = deque()
    dist = [[-1] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if world[i][j] == k:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                # 다른 육지일 때
                if world[nx][ny] > 0 and world[nx][ny] != k:
                    return dist[x][y]

                # 가보지 않은 바다일 때
                if world[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

# 섬 구분
for i in range(N):
    for j in range(N):
        if world[i][j] == 1 and visited[i][j] != world[i][j]:
            num_island += 1
            island(i, j, num_island)

# 섬간 최단거리 탐색
for i in range(2, num_island):
    minDist = min(minDist, find_bridge(i))

print(minDist)