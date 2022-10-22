# 백준 #14002 가장 긴 증가하는 부분 수열 4
'''
    Algorithm: dp
    Time Complexity: O(N^2)
'''
import sys

input = sys.stdin.readline
INF = 1001

def solution(N, nums):
    dp = [1] * (N+1)

    for i in range(N):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    answer = []
    max_dp = max(dp)
    print(max_dp)

    for i in range(N-1, -1, -1):
        if dp[i] == max_dp:
            answer.append(nums[i])
            max_dp -= 1
    
    print(*answer[::-1])


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    
    solution(N, A)