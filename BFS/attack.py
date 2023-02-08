# 백준 #1430 공격
'''
    Algorithm: bfs
    Time Complexity: O(N)

'''
import sys
import math
from typing import List, Tuple, Callable
from collections import deque

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    info = list(map(int, input().split()))
    towers = [tuple(map(int, input().split())) for _ in range(info[0])]
    return info, towers


def solution(info:List[int], towers:List[Tuple]) -> float:
    N, R, D, eX, eY = info
    total_damage = 0.0

    def get_dist(a:int, b:int, c:int, d:int) -> float:
        return math.sqrt((a-c)**2 + (b-d)**2)

    q = deque([(eX, eY, 0)])
    visited = set()

    while q:
        x, y, lev = q.popleft()
    
        for nx, ny in towers:
            if get_dist(x, y, nx, ny) <= R and (nx, ny) not in visited:
                q.append((nx, ny, lev+1))
                visited.add((nx, ny))
                total_damage += D / 2**lev        
    return total_damage


if __name__ == "__main__":
    print(solution(*read_data()))

