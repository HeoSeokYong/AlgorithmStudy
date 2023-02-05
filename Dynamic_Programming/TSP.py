# 백준 #2098 외판원 순회
'''
    Algorithm: dp, bit masking, tsp
    Time Complexity: -

    Traveling Salesman problem (TSP)

    모든 도시 탐색, 중복 탐색 x(시작 도시로 돌아오는 것 제외), 최소 비용
    도시의 수 N (2 <= N <= 16)

    dp를 INF로 초기화하고 하면 시간초과가 난다.
    => dp를 None으로 초기화하고 dp에 값을 넣을 때 변수를 INF로 선언하고
        해당 변수를 dp에 저장하는 식으로 해야 시간 초과가 안난다.
'''
import sys
from typing import List

sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = 16*1000000 + 1

def solution(N: int, W: List[List[int]]) -> int:
    dp = [[None for _ in range(1 << N)] for _ in range(N)]
    start_city = 0

    def dfs(cur_city: int, visited_city: int) -> int:
        ''' Top-down dp '''
        if visited_city == (1 << N) - 1:
            # 모든 도시를 방문하고, 시작 도시로 돌아가는 경로가 있는 경우 or 없는 경우
            return W[cur_city][start_city] or INF

        elif dp[cur_city][visited_city] == None:
            min_dist = INF
            for next_city in range(N): 
                if visited_city & (1 << next_city) or W[cur_city][next_city] == 0:
                    # 이미 방문했거나 경로가 없는 경우
                    continue
                # dp[cur_city][visited_city] = min(dp[cur_city][visited_city], dfs(next_city, visited_city | (1 << next_city)) + W[cur_city][next_city])
            
                min_dist = min(min_dist, dfs(next_city, visited_city | (1 << next_city)) + W[cur_city][next_city])
            
            dp[cur_city][visited_city] = min_dist

        return dp[cur_city][visited_city]

    return dfs(0, 1 << start_city)


if __name__ == "__main__":
    N = int(input())
    W = [list(map(int, input().split())) for _ in range(N)]

    print(solution(N, W))
