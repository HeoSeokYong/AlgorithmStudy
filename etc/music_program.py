# 백준 #2623 음악프로그램
'''
    Algorithm: 위상정렬
    Time Complexity: O(NM)

'''
import sys
from collections import deque

input = sys.stdin.readline

def solution(N, M):
    ''' 
        input = 가수의 수: N, 보조 PD의 수: M 
        output = 가수들의 출연 순서    
    '''
    order = []
    inDegree = [set() for _ in range(N+1)]
    outDegree = [set() for _ in range(N+1)]

    for _ in range(M):
        nums = list(map(int, input().split()))
        for i in range(1, nums[0]):
            for j in range(i, nums[0]):
                inDegree[nums[j+1]].add(nums[i])
                outDegree[nums[i]].add(nums[j+1])

    q = deque()
    visited = [False for _ in range(N+1)]

    for i in range(1, N+1):
        if not inDegree[i]:
            q.append(i)
            visited[i] = True

    while q:
        num = q.popleft()

        order.append(num)
        
        for x in outDegree[num]:
            inDegree[x].discard(num)
            if not inDegree[x] and not visited[x]:
                q.append(x)
                visited[x] = True

    if len(order) == N:
        for o in order:
            print(o)
    else:
        print(0)


if __name__ == "__main__":
    N, M = map(int, input().split())

    solution(N, M)