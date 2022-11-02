# 백준 #1334 다음 팰린드롬 수
'''
    Algorithm: 조건 분기
    Time Complexity: O(N) (N은 숫자의 자리수)
    
    중간점에서 왼쪽만 보면 될듯? 수를 중간을 기준으로 두개로 나누자.
    - 왼쪽 부분을 뒤집은 수 X
    - 오른쪽이 X보다 작을 경우, X로 바꾸고 리턴
    - 오른쪽이 X보다 클 경우, 왼쪽 부분에 1을 더하고 오른쪽을 변한 X로 바꾸고 리턴
'''
import sys

input = sys.stdin.readline

def solution(N):
    nums = list(N)
    flag = False
    
    while True:
        mid = (len(nums)+1) // 2

        left = nums[:mid]
        right = nums[mid:]

        if len(nums) % 2: # odd
            X = left[:-1][::-1] # 중간을 제외한 왼쪽 부분을 뒤집음

        else: # even
            X = left[::-1]
        
        if flag or X > right: # 같은 자리의 수만 비교하므로 리스트로 비교
            nums = left + X
            break

        else:
            lnum = int("".join(left)) + 1
            left = list(str(lnum))
            flag = True

        nums = left + right

    return "".join(nums)


if __name__ == "__main__":
    N = input().rstrip()

    print(solution(N))