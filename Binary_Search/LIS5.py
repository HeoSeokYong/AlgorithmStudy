# 백준 #14003 가장 긴 증가하는 부분 수열 5
'''
    Algorithm: binary search, LIS
    Time Complexity: O(NlogN)
'''
import sys

input = sys.stdin.readline

def solution(N, nums):
    answer = []
    seq = [nums[0]]
    # nums의 원소별 LIS를 만들었을때 들어갈 수 있는 위치를 저장
    dp = [0] * (N)

    def binary_search(l, r, val):
        while l < r:
            mid = (l+r) // 2
            
            if seq[mid] < val:
                l = mid + 1
            else:
                r = mid

        return r

    i = 1
    while i < N:
        if seq[-1] < nums[i]:
            seq.append(nums[i])
            dp[i] = len(seq) - 1
        else:
            dp[i] = binary_search(0, len(seq), nums[i])
            seq[dp[i]] = nums[i]

        i += 1

    max_dp = len(seq)
    print(max_dp)

    for i in range(N-1, -1, -1):
        if dp[i] == (max_dp - 1):
            answer.append(nums[i])
            max_dp -= 1

    print(*answer[::-1])

    
if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))

    solution(N, A)