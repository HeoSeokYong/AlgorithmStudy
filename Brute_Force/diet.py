# 백준 #19942 다이어트
'''
    Algorithm: brute-force, combination
    Time Complexity: -

    try 1) dfs를 사용한 브루트포스 -> 시간초과

    try 2) 조합을 사용해보자.
    조합이 더 느릴 줄 알았는데 더 빠르다.
'''
import sys
from typing import List, Tuple, Callable
from itertools import combinations

INF = float('inf')

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    nutrients = tuple(map(int, input().split()))
    foods = [tuple(map(int, input().split())) for _ in range(N)]
    return N, nutrients, foods

def solution(N:int, nutrients:Tuple, foods:List[Tuple]) -> int:
    result = [INF, None]

    def check(nut:List[int]):
        for i in range(4):
            if nut[i] < nutrients[i]:
                return False
        return True
    
    for i in range(1, N+1):
        for comb in combinations(range(1, N+1), i):
            nut = [0, 0, 0, 0, 0]
            for x in comb:
                for n in range(5):
                    nut[n] += foods[x-1][n]
        
            if nut[4] > result[0]:
                continue

            if check(nut):
                if result[0] > nut[4]:
                    result[0] = nut[4]
                    result[1] = comb
                elif result[0] == nut[4]:
                    result[1] = min(result[1], comb)
    
    if result[0] == INF:
        return [-1]

    return result[0], " ".join(list(map(str, result[1])))


if __name__ == "__main__":
    print(*solution(*read_data()), sep='\n')
