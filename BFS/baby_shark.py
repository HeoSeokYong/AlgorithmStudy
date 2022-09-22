import sys
import heapq
input = sys.stdin.readline

WATER = 0
BABY_SHARK = 9
dxdy = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def find_food(shark, sea):
    '''
        최소 힙을 통해 제일 작은 거리, x축, y축의 물고기 위치를 반환.
    '''
    N = len(sea)
    heap = []
    visited = [[False] * N for _ in range(N)]

    curx, cury = shark['loc']
    heapq.heappush(heap, (0, curx, cury))
    visited[curx][cury] = True

    while heap:
        d, x, y = heapq.heappop(heap)

        if sea[x][y] != WATER and sea[x][y] < shark['lev']:
            return d, (x, y)

        for dx, dy in dxdy:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < N and 0 <= ny < N \
            and sea[nx][ny] <= shark['lev'] and visited[nx][ny] == False:
                heapq.heappush(heap, (d+1, nx, ny))
                visited[nx][ny] = True

    return 0, ()

def explore(sea):
    N = len(sea)
    t, exp, num_fishes = 0, 0, 0
    
    # analysis sea
    for i in range(N):
        for j in range(N):
            if sea[i][j] == BABY_SHARK:
                shark = {'loc': (i, j), 'lev': 2}
            elif sea[i][j] != WATER:
                num_fishes += 1

    # explore sea
    while num_fishes:
        x, y = shark['loc']
        sea[x][y] = WATER

        dist, food = find_food(shark, sea)

        # call mom
        if not food:
            break

        # exp up
        exp = (exp+1) % shark['lev']

        # level up
        if exp == 0:
            shark['lev'] += 1 

        # move & eat fish
        shark['loc'] = food
        num_fishes -= 1

        # increase tishark
        t += dist

    return t

def solution():
    N = int(input())
    sea = [list(map(int, input().split())) for _ in range(N)]

    print(explore(sea))


if __name__ == "__main__":
    solution()