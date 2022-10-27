# 백준 #2314 이세계 게임
'''
    Algorithm: bfs
    Time Complexity: -
'''
import sys
from collections import deque

input = sys.stdin.readline
LP = {'L':1, 'P':0}

def solution(world, wanna):
    result = 0
    dxdy = ((0, 1), (0, -1), (1, 0), (-1, 0))
    # (0, 0) 부터 검사하여 wanna와 같은 경우 or 움직여서 같게 한 경우 True
    clear = [[False] * 4 for _ in range(4)]

    def bfs(i, j):
        ''' 가장 근처의 원하는 종족의 위치를 반환 '''
        target = wanna[i][j]
        q = deque([(i, j)])
        visited = set([(i, j)])

        while q:
            x, y = q.popleft()

            for dx, dy in dxdy:
                nx, ny = x+dx, y+dy

                if 0 <= nx < 4 and 0 <= ny < 4 and not clear[nx][ny] and (nx, ny) not in visited:
                    if world[nx][ny] == target:
                        return nx, ny
        
                    q.append((nx, ny))
                    visited.add((nx, ny))

    def move(x1, y1, x2, y2):
        ''' (x1, y1) 의 종족을 (x2, y2) 위치로 이동 '''
        while y1 < y2:
            tmp = world[x1][y1]
            world[x1][y1] = world[x1][y1+1]
            world[x1][y1+1] = tmp
            y1 += 1
            
        while y2 < y1:
            tmp = world[x1][y1]
            world[x1][y1] = world[x1][y1-1]
            world[x1][y1-1] = tmp
            y1 -= 1

        while x1 < x2:
            tmp = world[x1][y1]
            world[x1][y1] = world[x1+1][y1]
            world[x1+1][y1] = tmp
            x1 += 1
            
        while x2 < x1:
            tmp = world[x1][y1]
            world[x1][y1] = world[x1-1][y1]
            world[x1-1][y1] = tmp
            x1 -= 1

    for i in range(4):
        for j in range(4):
            if world[i][j] != wanna[i][j]:
                ni, nj = bfs(i, j)
                result += abs(ni - i) + abs(nj - j)
                move(ni, nj, i, j)

            clear[i][j] = True

    return result


if __name__ == "__main__":
    world = [[LP[x] for x in input().rstrip()] for _ in range(4)]
    input()
    wanna = [[LP[x] for x in input().rstrip()] for _ in range(4)]

    print(solution(world, wanna))