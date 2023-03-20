# 백준 #2262 토너먼트 만들기
'''
    Algorithm: greedy
    Time Complexity: O(N^2)
    
    어차피 우승은 1 -> 제일 큰 수부터 없애가자. (제일 큰 수는 양 옆이 누구든 진다.)

'''
import sys
from typing import List, Tuple, Callable

INF = float('inf')

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    ranking = [INF] + list(map(int, input().split())) + [INF]
    return N, ranking


def solution(N:int, ranking:List[int]) -> int:
    result = 0
    
    while N > 1:
        player_idx = ranking.index(N)
        
        # 가장 큰 수는 양 옆 중 차이가 적은 쪽에게 진다.
        result += min(abs(N - ranking[player_idx-1]), abs(N - ranking[player_idx+1]))
        
        del ranking[player_idx]
        N -= 1

    return result


if __name__ == "__main__":
    print(solution(*read_data()))
