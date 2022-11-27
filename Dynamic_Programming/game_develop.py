# 백준 #1516 게임 개발
'''
    Algorithm: dp
    Time Complexity: O(N^2)

'''
import sys
from collections import deque

input = sys.stdin.readline

def solution(N):
    '''
        input = N: 건물의 종류 수
        output = 각 건물이 완성되기까지 걸리는 최소 시간
    '''
    result = [0 for _ in range(N)]
    build_time = []
    prebuild, postbuild = [0 for _ in range(N+1)], [[] for _ in range(N+1)]
    q = deque()

    for i in range(N):
        inp = list(map(int, input().split()))
        build_time.append(inp[0])
        for j in range(1, len(inp)-1):
            prebuild[i+1] += 1
            postbuild[inp[j]].append(i+1)
        
    for i in range(1, N+1):
        if prebuild[i] == 0:
            q.append(i)
            result[i-1] = build_time[i-1]

    while q:
        cur = q.popleft()
        # 현재 건물 짓기

        for x in postbuild[cur]:
            prebuild[x] -= 1
            result[x-1] = max(result[cur-1] + build_time[x-1], result[x-1])
            if prebuild[x] == 0:
                q.append(x)

    return result


if __name__ == "__main__":
    N = int(input())

    print(*solution(N), sep='\n')