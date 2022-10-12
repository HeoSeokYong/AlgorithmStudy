# 백준 #21610 마법사 상어와 비바라기
'''
    알고리즘: 구현
    시간복잡도: O(N^2 * M)
'''
import sys

input = sys.stdin.readline
direction = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

def rain_dance(x):
    ''' 비바라기 마법 : 비구름을 반환'''
    return {'loc':{(x, 0), (x, 1), (x-1, 0), (x-1, 1)}}

def water_copy_bug(grid, loc):
    ''' 물복사 버그 마법 '''
    for x, y in loc:
        cnt = 0
        for i in range(2, 9, 2): # direction의 대각선 이동 정보
            dx, dy = direction[i]
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(grid) and 0 <= ny < len(grid) and grid[nx][ny] > 0:
                cnt += 1
        
        grid[x][y] += cnt

def form_cloud(grid, rain_cloud):
    ''' 구름 생성 '''
    loc = set()
    N = len(grid)

    for i in range(N):
        for j in range(N):
            if grid[i][j] >= 2 and (i, j) not in rain_cloud:
                loc.add((i, j))
                grid[i][j] -= 2
    
    return loc

def solution(N, M, grid, move):
    rain_cloud = rain_dance(N-1)

    for i in range(M):
        d, s = move[i]

        dx, dy = direction[d]
        dx, dy = dx * s, dy * s

        ncloud = set()
        for x, y in rain_cloud['loc']:
            nx = (x + dx) % N
            ny = (y + dy) % N

            grid[nx][ny] += 1
            ncloud.add((nx, ny))
        
        water_copy_bug(grid, ncloud)

        rain_cloud['loc'] = form_cloud(grid, ncloud)

    return sum([sum(g) for g in grid])


if __name__ == "__main__":
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    move = [tuple(map(int, input().split())) for _ in range(M)]

    print(solution(N, M, A, move))