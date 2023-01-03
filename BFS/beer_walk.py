# 백준 #9205 맥주 마시면서 걸어가기
'''
    Algorithm: bfs
    Time Complexity: O(N^2)

'''
import sys
from typing import List
from collections import deque

input = sys.stdin.readline

def get_dist(x1: int, y1: int, x2: int, y2: int) -> int:
        return abs(x2-x1) + abs(y2-y1)

def solution(N: int, loc: List[tuple]) -> str:
    targetX, targetY = loc.pop()
    visited = [False for _ in range(N)]

    q = deque([loc.pop(0)])

    while q:
        x, y = q.popleft()
        
        if get_dist(x, y, targetX, targetY) <= 1000:
            return "happy"

        for i in range(N):
            nx, ny = loc[i]
            if not visited[i] and get_dist(x, y, nx, ny) <= 1000:
                q.append((nx, ny))
                visited[i] = True

    return "sad"


if __name__ == "__main__":
    t = int(input())
    
    for test_case in range(t):
        N = int(input())
        loc = [tuple(map(int, input().split())) for _ in range(N+2)]

        print(solution(N, loc))