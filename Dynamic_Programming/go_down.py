# 백준 #2096 내려가기
'''
    Algorithm: dp
    Time Complexity: O(N)
'''
import sys

input = sys.stdin.readline
INF = sys.maxsize

def solution(N: int) -> tuple:
    scores = list(map(int, input().split()))
    dp_max = scores[:]
    dp_min = scores[:]
    tmp = [[0 for _ in range(3)] for _ in range(2)] # max, min
    
    for _ in range(1, N):
        scores = list(map(int, input().split()))
        for j in range(3):
            tmp[0][j] = max([dp_max[j+k] for k in (-1, 0, 1) if 0 <= j+k < 3]) + scores[j]
            tmp[1][j] = min([dp_min[j+k] for k in (-1, 0, 1) if 0 <= j+k < 3]) + scores[j]
                
        dp_max = tmp[0][:]
        dp_min = tmp[1][:]
    
    return max(dp_max), min(dp_min)


if __name__ == "__main__":
    N = int(input())

    print(*solution(N))