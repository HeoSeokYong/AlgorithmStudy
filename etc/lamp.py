# 백준 #1034 램프
'''
    Algorithm: 구현, 애드혹
    Time Complexity: O(NM)

    행마다 0을 카운트. 0의 개수가 k보다 작고 같은 홀수(or 짝수)일 경우,
    해당 행을 킬 수 있다.
    같은 모양의 행을 카운트하여 최대로 켤 수 있는 경우 체크
'''
import sys
from collections import defaultdict

input = sys.stdin.readline

def solution(N: int, M: int) -> int:
    result = 0 
    table = defaultdict(int)

    for _ in range(N):
        table[input().rstrip()] += 1

    K = int(input())

    for row in table:
        zero_cnt = row.count('0')

        if zero_cnt <= K and zero_cnt % 2 == K % 2:
            result = max(result, table[row])

    return result


if __name__ == "__main__":
    N, M = map(int, input().split())
    
    print(solution(N, M))