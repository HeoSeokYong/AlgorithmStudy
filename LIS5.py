# 백준 #14003 가장 긴 증가하는 부분 수열 5
'''
    Algorithm: binary search
    Time Complexity: O(NlogN)
    10.19 - 채점이 되기 시작했다... ~ 25% 까지 성공!
'''
from re import L
import sys

input = sys.stdin.readline

def solution(N, nums):
    seq = [nums[0]]
    # nums의 원소별 LCS를 만들었을때 들어갈 수 있는 위치를 저장
    dp = [(1, nums[0])]

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
            dp.append((len(seq), nums[i]))
        else:
            idx = binary_search(0, len(seq), nums[i])
            seq[idx] = nums[i]
            dp.append((idx, nums[i]))

        i += 1

    ls = len(seq)

    answer = [seq[0]]
    for i in range(N-1, -1, -1):
        
    # for i in range(ls-1, -1, -1):
    #     print(nums[lis[i]], end=' ')

    
if __name__ == "__main__":
    # N = int(input())
    # A = list(map(int, input().split()))
    N = 1000000
    A = [i+900000000 for i in range(N)]

    solution(N, A)