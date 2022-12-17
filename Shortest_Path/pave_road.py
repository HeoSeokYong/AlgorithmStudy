# 백준 #1162 도로포장
'''
    Algorithm: dijkstra
    Time Complexity: O(NKlogNK) ?

    다익스트라 알고리즘 with heap: (소요 시간, 포장한 도로의 수, 다음 도시)
'''
import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

def solution(N: int, M: int, K: int) -> int:
    road = [[] for _ in range(N+1)]
    dp = [[INF for _ in range(K+1)] for _ in range(N+1)]

    for _ in range(M):
        a, b, t = map(int, input().split())
        road[a].append((b, t))
        road[b].append((a, t))
    
    heap = [(0, 0, 1)]
    dp[1] = [0 for _ in range(K+1)]

    while heap:
        cur_time, k, city = heapq.heappop(heap)

        if dp[city][k] < cur_time:
            continue

        for next_city, thr_time in road[city]:
            # 이 도로를 포장 할 경우
            if k < K and cur_time < dp[next_city][k+1]:
                dp[next_city][k+1] = cur_time
                heapq.heappush(heap, (cur_time, k+1, next_city))
            # 포장하지 않을 경우
            if cur_time + thr_time < dp[next_city][k]:
                dp[next_city][k] = cur_time + thr_time
                heapq.heappush(heap, (cur_time + thr_time, k, next_city))

    # dp[N][K]가 안되는 이유 => 포장할 도로의 수가 도로의 수보다 많을 경우 INF가 나온다.
    return min(dp[N]) 
    

if __name__ == "__main__":
    N, M, K = map(int, input().split())

    print(solution(N, M, K))