'''
    brute-force
'''

import sys
import math
input = sys.stdin.readline

def solution(N, M, A):
    '''
        모든 행, 열에서 가능한 등차의 수의 집합 탐색
    '''
    maxS = -1

    for i in range(N):
        for j in range(M):
            for dx in range(-N, N):
                for dy in range(-M, M):
                    if dx == 0 and dy == 0:
                        continue
    
                    x, y = i, j
                    num = ''

                    while 0 <= x < N and 0 <= y < M:
                        # 시작 지점부터 값 넣어주기
                        num += A[x][y]

                        # 제곱 수일 경우 최대 제곱 수 갱신
                        sq_num = math.sqrt(int(num))
                        if sq_num.is_integer():
                            maxS = max(maxS, int(num))
                        
                        # 각 등차에 따른 다음 수
                        x = x + dx
                        y = y + dy

    return maxS
                        

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [input().rstrip() for _ in range(n)]

    print(solution(n, m, a))