'''
    좌->우, 우->좌 누적 최대공약수 구하기
    # 누적 합
'''
import sys
import math

input = sys.stdin.readline

def solution(N, nums):
    GCD, K = 0, 0

    gcdlr = [nums[0]] * N
    gcdrl = [nums[N-1]] * N

    for i in range(1, N):
        gcdlr[i] = math.gcd(gcdlr[i-1], nums[i])
        gcdrl[N-1-i] = math.gcd(gcdrl[N-i], nums[N-1-i])

    for i in range(N):
        if i == 0:
            gcd_cand = gcdrl[1]
        elif i == N-1:
            gcd_cand = gcdlr[-2]
        else:
            gcd_cand = math.gcd(gcdlr[i-1], gcdrl[i+1])

        if nums[i] % gcd_cand != 0 and GCD < gcd_cand:
            GCD = gcd_cand
            K = nums[i]

    if GCD and K:
        return GCD, K
    else:
        return [-1]


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))

    print(*solution(N, nums))