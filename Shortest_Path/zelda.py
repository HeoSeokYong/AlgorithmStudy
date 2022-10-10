'''
    알고리즘: 최소 힙, 다익스트라
    시간복잡도: O(NlogN)
'''
import sys
import heapq

input = sys.stdin.readline
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
INF = 1e6

def solution(N, cave):
    # 최소 힙을 사용해 최단 거리를 구함
    result = INF

    heap = [(cave[0][0], 0, 0)]

    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True
    
    while heap:
        r, x, y = heapq.heappop(heap)

        for dx, dy in direction:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                nr = r + cave[nx][ny]
                visited[nx][ny] = True
                if nx == N-1 and ny == N-1:
                    result = min(result, nr)
                else:
                    heapq.heappush(heap, (nr, nx, ny))

    return result


if __name__ == "__main__":
    prob_cnt = 0

    while N := int(input()):
        cave = [list(map(int, input().split())) for _ in range(N)]

        prob_cnt += 1
        print(f'Problem {prob_cnt}:', solution(N, cave))