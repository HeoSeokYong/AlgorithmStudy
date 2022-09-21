import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

def air_check(cheese):
    # 치즈 안의 공기가 없는 경우
    if True not in [0 in c for c in cheese]:
        return cheese

    # dfs
    deq = deque([(0, 0)])
    visited = [[False] * m for _ in range(n)]

    while deq:
        x, y = deq.pop()

        cheese[x][y] = -1
        visited[x][y] = True
        
        # 상하좌우의 방문하지 않은 공기를 스택에 넣음
        if x < n-1 and cheese[x+1][y] != 1 and visited[x+1][y] == False:
            deq.append((x+1, y))
        if x > 0 and cheese[x-1][y] != 1 and visited[x-1][y] == False:
            deq.append((x-1, y))
        if y < m-1 and cheese[x][y+1] != 1 and visited[x][y+1] == False:
            deq.append((x, y+1))
        if y > 0 and cheese[x][y-1] != 1 and visited[x][y-1] == False:
            deq.append((x, y-1))

    return cheese

def melt(cheese):
    cheese = air_check(cheese)
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    del_list = []

    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                cnt = 0
                for di, dj in dir:
                    if 0 <= i+di < n and \
                        0 <= j+dj < m and \
                        cheese[i+di][j+dj] == -1:
                        cnt += 1
                        if cnt == 2:
                            del_list.append((i, j))
                            break

    for x, y in del_list:
        cheese[x][y] = -1

    return cheese


cheese = [[x for x in map(int, input().split())] for _ in range(n)]
t = 0

while True:
    t += 1
    cheese = melt(cheese)
    
    # 전부 녹았는지 체크
    if True not in [1 in c for c in cheese]:
        break

print(t)
