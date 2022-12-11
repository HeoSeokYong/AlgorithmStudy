# 백준 #11066 파일 합치기
'''
    Algorithm: DP
    Time Complexity: O(K^3) ?

    파일을 합칠 때 순서가 맞아야 함.
    파일의 범위의 길이 별로 비용 (ex. 3일 때, 1 + 2,3 \ 1,2 + 3 ...)
    dp[i][j] = i ~ j 번째 까지 파일을 합치는 최소 비용
    비용 = 범위 안의 파일들을 합칠 때 드는 모든 비용 + 범위 안 모든 파일 비용의 합
    pypy3 통과, python3 시간초과.
'''
import sys

input = sys.stdin.readline

def solution() -> int:
    K = int(input())
    file_size = list(map(int, input().split()))
    dp = [[0 for _ in range(K+1)] for _ in range(K+1)]

    # 누적 합
    prefix = [0 for _ in range(K+1)]
    for i in range(K+1):
        prefix[i] = prefix[i-1] + file_size[i-1]

    for j in range(2, K+1): # 파일 범위의 길이
        for i in range(1, K-j+2): # 시작 파일 위치
            # k를 기준으로 나눔.
            dp[i][i+j-1] = min([dp[i][i+k] + dp[i+k+1][i+j-1] for k in range(j-1)]) + (prefix[i+j-1] - prefix[i-1])

    return dp[1][K]


if __name__ == "__main__":
    T = int(input())
    
    for test_case in range(T):
        K = int(input())
        file_size = list(map(int, input().split()))
        print(solution())


