# 백준 #1640 동전 뒤집기
'''
    Algorithm: 구현
    Time Complexity: O(NM)

    행, 열 별로 홀/짝 상태를 기록
    ex) 11
        01 
        row_state = [EVEN, ODD]
        col_state = [ODD, EVEN] 
    
    총 4가지의 경우가 가능하다.
    1. 행을 모두 even으로 바꾸고 열에 남은 odd의 개수가 짝수일때
    2. 행을 모두 odd로 바꾸고 열에 남은 odd의 개수가 홀수일때
    3. 열을 모두 even으로 바꾸고 행에 남은 odd의 개수가 짝수일때
    4. 열을 모두 odd로 바꾸고 행에 남은 odd의 개수가 홀수일때
    이 중 구해지는 값이 있을 경우 최솟값을 구하고, 없을 경우 -1을 반환한다.
'''
import sys
from typing import List, Tuple, Callable

EVEN, ODD = False, True
INF = float('inf')

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, M = map(int, input().split())
    coins = [list(input()) for _ in range(N)]
    return N, M, coins


def solution(N:int, M:int, coins:List[int]) -> int:
    result = INF
    row_state, col_state = [EVEN for _ in range(N)], [EVEN for _ in range(M)]
    
    def func(to_change:int, opp_odd:int, opp_even:int, state:bool) -> int:
        '''
            to_change: 바꿔야 될 동전의 개수
            opp_odd, opp_even: 반대편(행->열, 열->행)의 odd, even의 개수
            state: to_change로 바꿨을 때 행(열)의 전체 상태
        '''
        if to_change % 2:
            # 기준 행(열)을 바꾸는 횟수가 홀수인 경우 반대편의 상태가 반전된다. (짝수인 경우 그대로)
            opp_odd, opp_even = opp_even, opp_odd

        if opp_odd % 2 == state:
            # 반대편 odd를 바꾸는 횟수가 홀수일 경우 기준 행(열)의 상태도 반전되므로 두 값이 같아야 한다.
            return to_change + opp_odd

        return INF

    # main
    for i in range(N):
        for j in range(M):
            if coins[i][j] == '1': # back
                row_state[i] = not row_state[i]
                col_state[j] = not col_state[j]
    
    row_even = row_state.count(EVEN)
    row_odd = N - row_even
    col_even = col_state.count(EVEN)
    col_odd = M - col_even

    result = min(result, func(row_odd, col_odd, col_even, EVEN)) # 1 
    result = min(result, func(row_even, col_odd, col_even, ODD)) # 2 
    result = min(result, func(col_odd, row_odd, row_even, EVEN)) # 3
    result = min(result, func(col_even, row_odd, row_even, ODD)) # 4 

    return result if result != INF else -1


if __name__ == "__main__":
    print(solution(*read_data()))
