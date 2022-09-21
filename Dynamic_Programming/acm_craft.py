'''
    T : testcase 개수
    N : 건물의 개수(1 ~ N)
    K : 건물간의 건설순서 규칙의 총 개수
'''

import sys
from collections import deque
input = sys.stdin.readline

# # 재귀 함수 -> 시간 초과
# def building(W):
#     if len(build_order[W]) == 0:
#         return build_time[W]
#     else:
#         return max(building(x) for x in build_order[W]) + build_time[W]

T = int(input())

for testcase in range(T):
    N, K = map(int, input().split())

    build_time = {i+1:x for i, x in enumerate(list(map(int, input().split())))}
    build_rule = [set() for _ in range(N+1)]

    dp = [0 for i in range(N+1)] # 해당 건물을 짓기까지 걸리는 시간
    num_parents = [0 for i in range(N+1)] # 부모 노드 개수
    
    for i in range(K):
        x, y = map(int, input().split())
        build_rule[x].add(y)
        num_parents[y] += 1

    # 루트 노드를 queue에 저장
    deq = deque()
    for i in range(1, N+1):
        if num_parents[i] == 0:
            deq.append(i)
            dp[i] = build_time[i]

    while deq:
        idx = deq.popleft()

        for x in build_rule[idx]:
            num_parents[x] -= 1
            dp[x] = max(dp[x], dp[idx] + build_time[x])
            # 해당 노드의 모든 경우의 수를 다 고려했을 때 큐에 추가
            if num_parents[x] == 0:
                deq.append(x)

    target = int(input())
    print(dp[target])