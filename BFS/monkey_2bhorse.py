# 백준 #1600 말이 되고픈 원숭이
'''
    Algorithm: bfs
    Time Complexity: O(N)?? (N = W*H*K)
'''
import sys
from collections import deque

input = sys.stdin.readline
INF = 1e6
move = {'monkey': ((0, 1), (0, -1), (1, 0), (-1, 0)), \
        'horse': ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))}

def solution(K, W, H, world):
    visited = [[[INF] * (K+1) for w in range(W)] for _ in range(H)]
    visited[0][0][K] = 0
    q = deque([(K, 0, 0)])
        
    while q:
        k, x, y = q.popleft()

        if x == H-1 and y == W-1:
            return visited[x][y][k]

        # horse move
        if k > 0:
            for dx, dy in move['horse']:
                nx, ny = x + dx, y + dy

                if 0 <= nx < H and 0 <= ny < W and world[nx][ny] != 1 and visited[nx][ny][k-1] > visited[x][y][k] + 1:
                    visited[nx][ny][k-1] = visited[x][y][k] + 1
                    q.append((k-1, nx, ny))

        # monkey move
        for dx, dy in move['monkey']:
            nx, ny = x + dx, y + dy

            if 0 <= nx < H and 0 <= ny < W and world[nx][ny] != 1 and visited[nx][ny][k] > visited[x][y][k] + 1:
                visited[nx][ny][k] = visited[x][y][k] + 1
                q.append((k , nx, ny))
    
    return -1


if __name__ == "__main__":
    K = int(input())
    W, H = map(int, input().split())
    world = [list(map(int,input().split())) for _ in range(H)]

    print(solution(K, W, H, world))
