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
INF = 10**8

def solution(N, M):
    arr = [list(map(int, input().split())) for _ in range(N)]
    dp = [[-INF for _ in range(M)] for _ in range(N)]

    dp[0][0] = arr[0][0]

    # 첫 열은 오른쪽으로 가는 경우밖에 없음.(왼쪽 x)
    for j in range(1, M):
        dp[0][j] = dp[0][j - 1] + arr[0][j]

    ltor, rtol = [0] * M, [0] * M

    for i in range(1, N):
        # left -> right
        ltor[0] = dp[i-1][0] + arr[i][0]
        for j in range(1, M):
            ltor[j] = max(dp[i-1][j], ltor[j-1]) + arr[i][j]

        # right -> left
        rtol[-1] = dp[i-1][-1] + arr[i][-1]
        for j in range(M-2, -1, -1):
            rtol[j] = max(dp[i-1][j], rtol[j+1]) + arr[i][j]

        # dp 갱신
        for j in range(M):
            dp[i][j] = max(ltor[j], rtol[j])    

    return dp[N-1][M-1]


if __name__ == "__main__":
    N, M = map(int, input().split())
    
    print(solution(N, M))