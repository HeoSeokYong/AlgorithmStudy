# 백준 #11404 플로이드
'''
    Algorithm: 플로이드-워셜 알고리즘
    Time Complexity: O(N^3)

    (2 <= N <= 100)
    1. 하나의 정점에서 다른 정점으로 갈 수 있으면 최소 비용을, 없다면 INF로 저장
    2. 거쳐가는 정점을 설정한 후 해당 정점을 거쳐가서 비용이 줄어드는 경우에는 값을 바꿔준다.
    3. 위 과정을 반복하여 모든 정점 사이의 최단 경로 탐색.
'''
import sys
from typing import List

input = sys.stdin.readline
INF = sys.maxsize

def solution(N: int, M: int) -> List[List[int]]:
    dist = [[INF for _ in range(N)] for _ in range(N)]

    for i in range(N):
        dist[i][i] = 0

    # 1
    for _ in range(M):
        a, b, c = map(int, input().split())
        dist[a-1][b-1] = min(dist[a-1][b-1], c)
    
    # 2, 3
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return [[d if d != INF else 0 for d in di] for di in dist]


if __name__ == "__main__":
    N = int(input())
    M = int(input())

    print(*map(lambda x: " ".join(map(str, x)), solution(N, M)), sep='\n')


''' 2022.09 에 풀었던 풀이
import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
dist = [[INF] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = min(dist[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# for i in range(n):
#     print(" ".join(map(str, dist[i])))

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()

'''