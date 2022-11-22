# 백준 #5569 출근경로
'''
    Algorithm: dp
    Time Complexity: O(WH)

    - bfs는 시간초과. 
'''
import sys

input = sys.stdin.readline
StrUp, CurUp, StrRt, CurRt = 0, 1, 2, 3 

def solution(w, h):
    dp = [[[0] * 4 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if i == 0:
                dp[i][j][StrRt] = 1
            elif j == 0:
                dp[i][j][StrUp] = 1
            else:
                # straight up check
                dp[i][j][StrUp] = dp[i-1][j][StrUp] + dp[i-1][j][CurUp]
                # curve up check
                dp[i][j][CurUp] = dp[i-1][j][StrRt]
                # straight right check
                dp[i][j][StrRt] = dp[i][j-1][StrRt] + dp[i][j-1][CurRt]
                # curve right check
                dp[i][j][CurRt] = dp[i][j-1][StrUp]

    return sum(dp[h-1][w-1]) % 100000


if __name__ == "__main__":
    w, h = map(int, input().split())

    print(solution(w, h))