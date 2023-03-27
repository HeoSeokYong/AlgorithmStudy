# 백준 #2617 구슬 찾기
'''
    Algorithm: 플로이드-워셜
    Time Complexity: O(N^3)

    앞 번호의 구슬이 뒤 번호의 구슬보다 무거움.
'''
import sys
from typing import Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, M = map(int, input().split())
    return N, M


def solution(N:int, M:int) -> int:
    result = 0
    rank = [[False for _ in range(N)] for _ in range(N)] # 0: light, 1: heavy

    for _ in range(M):
        h, l = map(int, input().split())
        rank[h-1][l-1] = True
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if rank[i][k] and rank[k][j]:
                    rank[i][j] = True
                
    for i in range(N):
        # 자신(i번 구슬)보다 가벼운/무거운 구슬의 개수
        light_cnt, heavy_cnt = 0, 0
        
        for j in range(N):
            if rank[i][j]:
                light_cnt += 1
            elif rank[j][i]:
                heavy_cnt += 1
        
        if light_cnt > N // 2 or heavy_cnt > N // 2:
            result += 1
        
    return result


if __name__ == "__main__":
    print(solution(*read_data()))
