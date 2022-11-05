# 백준 #2169 로봇 조종하기
'''
    Algorithm: dp
    Time Complexity: O(NM)

    같은 행에서 갔던 길을 돌아오는 것을 조심.
    top-down => 시간초과
    한가지 방향으로 업데이트(좌->우, 우->좌)
'''
import sys

input = sys.stdin.readline
dx = (0, 0, 1) # R L D
dy = (1, -1, 0)

def solution(N, M):
    INF = 10**8
    arr = [list(map(int, input().split())) for _ in range(N)]
    dp = [[-INF for _ in range(M)] for _ in range(N)]

    dp[0][0] = arr[0][0]
    
    for j in range(1, M):
        dp[0][j] = dp[0][j - 1] + arr[0][j]

    # 각 행 별 최대 dp를 구함
    for i in range(1, N):
        left2right, right2left = [0] * M, [0] * M

        left2right[0] = dp[i-1][0] + arr[i][0]
        for j in range(1, M):
            left2right[j] += max(dp[i-1][j], left2right[j-1]) + arr[i][j]

        right2left[-1] = dp[i-1][-1] + arr[i][-1]
        for j in range(M-2, -1, -1):
            right2left[j] += max(dp[i-1][j], right2left[j+1]) + arr[i][j]

        for j in range(M):
            dp[i][j] = max(left2right[j], right2left[j])    

    return dp[N-1][M-1]


if __name__ == "__main__":
    N, M = map(int, input().split())
    
    print(solution(N, M))