# 백준 #10711 모래성 
'''
    Algorithm: 구현
    Time Complexity: O(HW)

    1 <= H,W <= 1,000

    try 1) 완전 탐색 단순 구현 -> 시간 초과

    try 2) 무너질 곳만 처리해보자.
'''
import sys
from typing import List

input = sys.stdin.readline

def solution(H: int, W: int, castle: List[List[str]]) -> int:
    result = 0
    sand = []
    dxdy = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))

    def wave() -> List[tuple]:
        ''' 파도가 친 후 무너질 모래성의 좌표를 반환하는 함수 '''
        fallen_castle = []
        for i, j in sand:
            for di, dj in dxdy:
                ni, nj = i + di, j + dj

                if 0 < ni < H-1 and 0 < nj < W-1 and castle[ni][nj] > 0:
                    castle[ni][nj] -= 1
                    if castle[ni][nj] == 0:
                        fallen_castle.append((ni, nj))

        return fallen_castle

    for i in range(H):
        for j in range(W):
            if castle[i][j] == 0:
                sand.append((i, j))

    while sand := wave():
        result += 1

    return result


if __name__ == "__main__":
    H, W = map(int, input().split())
    castle = [[int(x) if x.isdigit() else 0 for x in list(input().rstrip())] for _ in range(H)]

    print(solution(H, W, castle))