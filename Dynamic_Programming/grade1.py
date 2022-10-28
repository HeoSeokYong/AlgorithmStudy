# 백준 #5557 1학년
'''
    Algorithm: dp
    Time Complexity: O(N)
    
    dp: 각 숫자마다 가능한 경우의 수
'''
import sys

input = sys.stdin.readline

def solution(N, nums):
    answer = nums.pop()
    dp = [[0] * 21 for _ in range(N-1)]
    dp[0][nums[0]] = 1

    for i in range(1, N-1):
        for j in range(21):
            if j + nums[i] <= 20:
                dp[i][j + nums[i]] += dp[i-1][j]
            if j - nums[i] >= 0:
                dp[i][j - nums[i]] += dp[i-1][j]

    return dp[-1][answer]


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))

    print(solution(N, nums))