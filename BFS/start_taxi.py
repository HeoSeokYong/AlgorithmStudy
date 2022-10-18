# 백준 #19238 스타트 택시
'''
    알고리즘: bfs(최소힙)
    시간복잡도: O(N^2 * 2N^2logN^2) = O(4N^4logN) = 약 300만
'''
import sys
import heapq

input = sys.stdin.readline
dxdy = ((-1, 0), (0, -1), (0, 1), (1, 0))

def solution(N, M, fuel, maps, r, c, passengers):
    taxi = (r, c)
    
    def nearest_passenger(r, c):
        ''' 가장 가까운 승객과 그 거리를 리턴 '''
        heap = [(0, r, c)]
        visited = set([(r, c)])
        
        while heap:
            d, x, y = heapq.heappop(heap)

            # 승객일 경우
            if maps[x][y] > 1:
                return d, x, y

            for dx, dy in dxdy:
                nx, ny = x + dx, y + dy

                if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                    if maps[nx][ny] != 1: # 갈 수 있는 곳
                        heapq.heappush(heap, (d+1, nx, ny))
                        visited.add((nx, ny))

        # 갈 수 있는 승객이 없는 경우 -1 리턴
        return -1, -1, -1

    def find_dest(px, py):
        ''' 승객을 목적지까지 데려다주는 비용 '''
        destX, destY = passengers[(px, py)]

        heap = [(0, px, py)]
        visited = set([(px, py)])

        while heap:
            d, x, y = heapq.heappop(heap)

            for dx, dy in dxdy:
                nx, ny = x + dx, y + dy

                if 0 <= nx < N and 0 <= ny < N and (nx,ny) not in visited and maps[nx][ny] != 1:
                    if nx == destX and ny == destY:
                        return d+1

                    heapq.heappush(heap, (d+1, nx, ny))
                    visited.add((nx, ny))

        # 데려다 줄 길이 없는 경우 -1 리턴
        return -1

    for _ in range(M):
        x, y = taxi
        # l1: 해당 승객을 데리러 가는데 필요한 연료
        l1, px, py = nearest_passenger(x, y)

        if l1 == -1:
            return -1

        # l2: 해당 승객을 목적지까지 데려다 주기 위해 필요한 연료
        l2 = find_dest(px, py)

        # 목적지로 가지 못하거나 남은 연료보다 소모량이 클 경우 종료
        if l2 == -1 or fuel < l1+l2:
            return -1
        
        # 택시와 승객의 정보 갱신
        taxi = passengers[(px, py)]
        maps[px][py] = 0

        # 연료 갱신
        fuel = fuel - l1 + l2
                    
    return fuel


if __name__ == "__main__":
    N, M, L = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    start_r, start_c = map(int, input().split())

    passengers = dict()
    for i in range(2, M+2):
        x1, y1, x2, y2 = tuple(map(int, input().split()))
        maps[x1-1][y1-1] = i
        passengers[(x1-1, y1-1)] = (x2-1, y2-1)

    print(solution(N, M, L, maps, start_r-1, start_c-1, passengers))