# 백준 #10942 팰린드롬?
'''
    Algorithm: Manacher Algorithm
    Time Complexity: O(M+N)
    155824 KB	1736 ms

    구현 참고 블로그: https://ialy1595.github.io/post/manacher/
'''
import sys

input = sys.stdin.readline

def solution(N):
    nums = []
    for x in map(int, input().split()):
        nums.extend([0, x])
    nums.append(0)

    M = int(input())
    questions = [tuple(map(int, input().split())) for _ in range(M)]

    dp = [0] * len(nums)
    p = r = 0

    for i in range(len(nums)):
        if r < i:
            p = r = i
            while r < len(nums) and r <= 2*p and nums[r] == nums[2*p - r]:
                r += 1
            r -= 1
            dp[i] = r - p

        else:
            j = 2*p - i

            if dp[j] < r - i:
                dp[i] = dp[j]
            
            elif dp[j] > r - i:
                dp[i] = r - i
            
            else: # dp[j] == r - i
                p = i
                while r < len(nums) and r <= 2*p and nums[r] == nums[2*p - r]:
                    r += 1
                r -= 1
                dp[i] = r - p

    for s, e in questions:
        ns, ne = 2*s-1, 2*e-1
        if dp[(ns+ne) // 2] >= e - s + 1:
            print(1)
        else:
            print(0)

    
if __name__ == "__main__":
    N = int(input())
    
    solution(N)

# ------------------------------------------------ #
# '''
#     Algorithm: dp
#     Time Complexity: O(N^2)
#     186228 KB,	2152 ms
#     길이 1: 팰린드롬
#     길이 2: 같을 경우 팰린드롬
#     길이 3이상: 양 끝이 같고 가운데가 팰린드롬이면 팰린드롬
# '''
# import sys

# input = sys.stdin.readline

# def solution(N, M, nums, questions):
#     dp = [[0] * N for _ in range(N)]
    
#     # 길이 1
#     for i in range(N):
#         dp[i][i] = 1 

#     # 길이 2
#     for i in range(N-1):
#         if nums[i] == nums[i+1]:
#             dp[i][i+1] = 1

#     # 길이 3 이상
#     for i in range(N-1, -1, -1):
#         for j in range(N-1, i-1, -1):
#             if j - i > 1 and nums[i] == nums[j] and dp[i+1][j-1]:
#                     dp[i][j] = 1

#     for s, e in questions:
#         print(dp[s-1][e-1])


# if __name__ == "__main__":
#     N = int(input())
#     nums = list(map(int, input().split()))
#     M = int(input())
#     questions = [tuple(map(int, input().split())) for _ in range(M)]

#     solution(N, M, nums, questions)