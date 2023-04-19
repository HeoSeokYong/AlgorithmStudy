# 백준 #2157 여행
'''
    Algorithm: dijkstra
    Time Complexity: TlogT (T: MN^2)

    서쪽으로만 이동 -> 도시 번호가 증가하는 순서대로만 이동 가능
    M개 이하의 도시만 지나는 계획
    먹게 되는 기내식의 점수의 총 합이 최대 -> 이동 비용을 최대로
'''
import sys
import heapq
from typing import List, Tuple, Callable
from collections import defaultdict


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, M, K = map(int, input().split())
    airlines = [defaultdict(int) for _ in range(N+1)]

    for _ in range(K):
        a, b, c = map(int, input().split())
        
        if a < b:
            airlines[a][b] = max(airlines[a][b], c)

    return N, M, K, airlines


def solution(N:int, M:int, K:int, airlines:List[List[int]]) -> int:
    score = [0 for _ in range(N+1)]

    heap = [(1, 0, 1)] # m_cnt, sum_score, loc
    
    while heap:
        cnt, sco, loc = heapq.heappop(heap)

        if cnt == M:
            break

        if score[loc] < sco:
            continue

        for k in airlines[loc].keys():
            if score[k] < airlines[loc][k] - sco:
                score[k] = airlines[loc][k] - sco
                heapq.heappush(heap, (cnt + 1, sco - airlines[loc][k], k))

    return score[N]


if __name__ == "__main__":
    print(solution(*read_data()))
