# 백준 #2342 Dance Dance Revolution
'''
    Algorithm: dp (top-down)
    Time complexity: -

    try 1) greedy
    - 그리디의 경우 최적해를 얻어내지 못했다. (반례: 2 1 3 2 3 0)
    -> dp로 최적해를 찾아보자.
    try 2) dp
    - 발의 위치가 l, r일 때 왼발을 움직일때 드는힘, 오른발을 움직일때 드는힘 중 최솟값
'''
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solution(orders):
    dp = [[[-1] * 5 for _ in range(5)] for _ in range(len(orders))]

    def get_force(cur, dist):
        ''' 각 다리를 움직이는데 필요한 에너지 '''
        if cur == 0:
            return 2
        elif abs(cur - dist) == 2: # 반대편
            return 4 
        elif cur == dist: # 같은 곳
            return 1
        else: # 인접
            return 3

    def ddr(l, r, x):
        ''' 발이 l, r 일 때 x번 발판을 밟는데 필요한 최소 힘 '''
        if x == len(orders)-1:
            return 0
        if dp[x][l][r] != -1:
            return dp[x][l][r]

        dp[x][l][r] = min(ddr(orders[x], r, x + 1) + get_force(l, orders[x]), ddr(l, orders[x], x + 1) + get_force(r, orders[x]))

        return dp[x][l][r]

    return ddr(0, 0, 0)

if __name__ == "__main__":
    orders = list(map(int, input().split()))

    print(solution(orders))