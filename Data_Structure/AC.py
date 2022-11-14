# 백준 #5430 AC
'''
    Algorithm: 구현, 덱
    Time Complexity: O(TN) (N: p의 갯수)
'''
import sys
from collections import deque

input = sys.stdin.readline

def solution():
    p = input().rstrip()
    n = int(input())
    nums = deque([x for x in input().strip('[]\n').split(',') if x])
    reverse = False

    for comm in p:
        if comm == 'R':
            reverse = not reverse

        elif comm == 'D':
            if not nums:
                return 'error'
            if reverse:
                nums.pop()
            else:
                nums.popleft()
    
    if reverse:
        nums.reverse()

    return '[' + ",".join(nums) + ']'


if __name__ == "__main__":
    T = int(input())

    for test in range(T):
        print(solution())

# ------------------------------------------------------------
'''
    Algorithm: 투포인터
    Time Complexity: O(TN) (N: p의 갯수)
'''
import sys

input = sys.stdin.readline

def solution():
    p = input().rstrip()
    n = int(input())
    nums = [x for x in input().strip('[]\n').split(',') if x]
    l, r = 0, n-1
    reverse = False

    for comm in p:
        if comm == 'R':
            reverse = not reverse

        elif comm == 'D':
            if l > r:
                return 'error'
            elif reverse:
                r -= 1
            else:
                l += 1

    result = nums[l:r+1]

    if reverse:
        result = result[::-1]

    return '[' + ",".join(result) + ']'


if __name__ == "__main__":
    T = int(input())

    for test in range(T):
        print(solution())