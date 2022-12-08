# 백준 #1766 문제집
'''
    Algorithm: 위상정렬, 최소힙
    Time Complexity: P(NlogN + M)

    위상 정렬과 최소힙을 사용해 적합한 문제 풀이 순서를 출력한다.
'''
import sys
import heapq

input = sys.stdin.readline

def solution(N: int, info: list[tuple]) -> list[int]:
    result = []

    in_degree_cnt = [0 for _ in range(N+1)]
    out_degree = [[] for _ in range(N+1)]

    for a, b in info:
        in_degree_cnt[b] += 1
        out_degree[a].append(b)

    heap = []
    visited = [False for _ in range(N+1)]

    for i in range(1, N+1):
        if in_degree_cnt[i] == 0:
            heapq.heappush(heap, i)
            visited[i] = True

    while heap:
        prob = heapq.heappop(heap)
        result.append(prob)

        for nprob in out_degree[prob]:
            in_degree_cnt[nprob] -= 1
            
            if in_degree_cnt[nprob] == 0 and not visited[nprob]:
                heapq.heappush(heap, nprob)
                visited[nprob] = True

    return result


if __name__ == "__main__":
    N, M = map(int, input().split())
    info = [tuple(map(int, input().split())) for _ in range(M)]

    print(*solution(N, info))