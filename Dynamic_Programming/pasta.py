# 백준 #5546 파스타
'''
    Algorithm: dp
    Time Complexity: O(N)

    try 1) 재귀를 사용해 풀어보자.(dfs) -> 시간초과
    
    try 2) dp
    dp[i][j][k] = i 번째 날에 j 파스타를 k+1번 연속 먹은 경우의 수
        (3 <= i <= 100, j = 3, k = 2)
    
    dp[i][j][0] = i-1번 날에 j파스타를 제외한 나머지 파스타의 모든 경우의 수의 합
    dp[i][j][1] = i-1번 날에 j파스타를 1번 먹은 경우의 수
'''
import sys

input = sys.stdin.readline

def solution(N: int, K: int) -> int:
    dp = [[[0] * 2 for _ in range(3)] for _ in range(N+1)]
    pasta = dict()
    
    for _ in range(K):
        a, b = map(int, input().split())
        for j in range(3):
            pasta[a] = b-1

    for i in range(1, N+1):
        for j in range(3):
            if i == 1:
                if i in pasta and j != pasta[i]:
                    continue
                dp[i][j][0] = 1

            else:
                if i in pasta and j != pasta[i]:
                    continue
                dp[i][j][0] = sum([sum(dp[i-1][x]) for x in range(3) if x != j]) % 10000
                dp[i][j][1] = dp[i-1][j][0]

    return sum([sum(x) for x in dp[-1]]) % 10000


if __name__ == "__main__":
    N, K = map(int, input().split())

    print(solution(N, K))