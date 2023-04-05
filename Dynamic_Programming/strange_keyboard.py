# 백준 #1796 신기한 키보드
'''
    Algorithm: dp
    Time Complexity: -

    알파벳 순서로 클릭.
    ex) 'e'의 최소 위치와 최대 위치 사이를 움직이면 모든 'e'를 클릭할 수 있다.

    dp[i][j] : 현재 커서가 i일때, j번째 알파벳을 모두 클릭하기 위해 필요한 최소 이동 횟수 
'''
import sys
from typing import List, Tuple, Callable

INF = sys.maxsize

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    S = list(input())
    return S,

def ctoi(c:str) -> int:
    return ord(c) - ord('a')

def solution(S:List[str]) -> int:
    N = len(S)
    alp_info = [None for _ in range(26)] # [최소 위치, 최대 위치]
    dp = [[INF for _ in range(26)] for _ in range(N)]
    
    def click(cur:int, dest:int, l:int, r:int) -> int:
        '''
            이동 비용을 계산: cur -> l -> r -> dest
        '''
        return abs(cur - l) + abs(l - r) + abs(r - dest)

    def keyboard(cur:int, alp:int):
        '''
            cur : 현재 위치
            alp : 클릭할 문자 인덱스
        '''
        if alp == 26:
            return 0
        
        if dp[cur][alp] == INF:
            if alp_info[alp]:
                mind, maxd = alp_info[alp]

                # 모든 위치를 검사하여 최적의 경로를 찾는다. 
                for i in range(N):
                    dp[cur][alp] = min(dp[cur][alp], min(click(cur, i, mind, maxd), click(cur, i, maxd, mind)) + keyboard(i, alp+1))
            
            else:
                dp[cur][alp] = keyboard(cur, alp+1)

        return dp[cur][alp]

    # main
    for i in range(len(S)):
        idx = ctoi(S[i])
        if alp_info[idx]:
            alp_info[idx][1] = i
        else:
            alp_info[idx] = [i, i]

    return keyboard(0, 0)  + N # N번의 클릭


if __name__ == "__main__":
    print(solution(*read_data()))
