# 백준 #1507 궁금한 민호
'''
    Algorithm: 플로이드-워셜
    Time Complexity: O(N^3)

    플로이드-워셜
    - 최소 거리가 갱신될 경우 -> -1 반환
    - 최소 거리와 같을 경우 i-j 경로를 없앤다. (많은 도시를 연결하기 위해)

'''
import sys
from typing import List, Tuple, Callable

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    dist = [list(map(int, input().split())) for _ in range(N)]
    return N, dist


def solution(N:int, dist:List[List[int]]) -> int:
    # floyd-warshall
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][k] != 0 and dist[k][j] != 0 and dist[i][j] != 0:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        return -1
                    elif dist[i][k] + dist[k][j] == dist[i][j]:
                        dist[i][j] = dist[j][i] = 0

    return sum(map(sum, dist)) // 2


if __name__ == "__main__":
    print(solution(*read_data()))

