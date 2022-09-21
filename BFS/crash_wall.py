import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[[0, 0] for _ in range(m)] for __ in range(n)]

world = []
for i in range(n):
    world.append(list(map(int, input().strip())))

q = deque()
q.append((0, 0, 0))
visited[0][0][0] = 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
flag = True

while q:
    x, y, z = q.popleft()
    if x == n-1 and y == m-1:
        flag = False
        print(visited[x][y][z])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        # 벽인데 파괴 가능
        if world[nx][ny] == 1 and z==0:
            q.append((nx, ny, 1))
            visited[nx][ny][1] = visited[x][y][0] + 1
        # 벽 아니고 방문 x
        elif world[nx][ny] == 0 and visited[nx][ny][z] == 0:
            q.append((nx, ny, z))
            visited[nx][ny][z] = visited[x][y][z] + 1

if flag: print(-1)