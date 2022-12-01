# 백준 #10423 전기가 부족해
'''
    Algorithm: prim algorithm
    Time Complexity: O(MlogN)

    도시를 탐색하며 발전소가 2개 이상 나온 순간부터 그 전의 
    케이블 중 가장 높은 cost의 케이블을 빼준다.
'''
import sys
import heapq

input = sys.stdin.readline

def solution(N, M, K):
    answer = 0
    power = set(map(int, input().split()))
    cable = [[] for _ in range(N+1)]

    for _ in range(M):
        u, v, w = map(int, input().split())
        cable[u].append((v, w))
        cable[v].append((u, w))

    heap = [(0, 1)]
    visited = [False for _ in range(N+1)]
    city = []
    power_cnt = 0

    while heap:
        cost, node = heapq.heappop(heap)

        if visited[node]:
            continue

        heapq.heappush(city, (-cost, node))
        answer += cost
        visited[node] = True

        if node in power:
            power_cnt += 1
            if power_cnt > 1:
                answer += heapq.heappop(city)[0]
            city = []
        
        for v, w in cable[node]:
            if not visited[v]:
                heapq.heappush(heap, (w, v))

    return answer


if __name__ == "__main__":
    N, M, K = map(int, input().split())

    print(solution(N, M, K))