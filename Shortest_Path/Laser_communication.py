# 백준 #6087 레이저 통신
'''
    Algorithm: 다익스트라, bfs
    Time Complexity: O(NlogN) - N = 4*W*H
    거리 기반이 아닌 거울의 개수를 기준으로 해야 할듯 하다.
'''
import sys
import heapq

input = sys.stdin.readline
INF = 1e6

def solution(W, H, maps):
    dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # 해당 위치를 갈 수 있는 최소 거울의 수
    dp_mirror = [[INF]*W for _ in range(H)]
    # 해당 위치에 도착했을 때의 방향과 거울의 수를 저장
    dir_dicts = [[dict() for _ in range(W)] for _ in range(H)]

    # C 하나의 위치 찾기
    for i in range(H):
        if 'C' in maps[i]:
            cx, cy = i, maps[i].index('C')
            dp_mirror[cx][cy] = -1
            break
    
    heap = [] # (거울의 수, x, y)
    for i in range(4):
        dx, dy = dxdy[i]
        nx, ny = cx + dx, cy + dy

        if 0 <= nx < H and 0 <= ny < W and maps[nx][ny] != '*':
            heapq.heappush(heap, (0, nx, ny))
            dir_dicts[nx][ny][i] = 0

    while heap:
        m, x, y = heapq.heappop(heap)

        if maps[x][y] == 'C':
            return m

        for i in range(4):
            dx, dy = dxdy[i]
            nx, ny = x + dx, y + dy
            # x, y 까지 도착했던 경로 중 방향이 이어지면 그 때의 거울 수를 가져오고
            # 방향을 꺾어야 할 경우 현재 거울 수 + 1
            nm = dir_dicts[x][y][i] if i in dir_dicts[x][y] else m+1

            if 0 <= nx < H and 0 <= ny < W and maps[nx][ny] != '*':
                if dp_mirror[nx][ny] >= nm:
                    if dp_mirror[nx][ny] > nm:
                        heapq.heappush(heap, (nm, nx, ny))

                    dp_mirror[nx][ny] = nm
                    dir_dicts[nx][ny][i] = nm
    
    return -1


if __name__ == "__main__":
    W, H = map(int, input().split())
    maps = [input() for _ in range(H)]

    print(solution(W, H, maps))