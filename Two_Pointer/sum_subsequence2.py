'''
    부분수열의 합 2
    부분수열의 개수: 2^N
    2^40 은 너무 크기때문에 -> 약 백만^2
    2^20 두개로 나눔 -> 약 이백만
    투 포인터
'''
import sys
from itertools import combinations

input = sys.stdin.readline

def get_sub_sum(seq):
    '''
        seq의 각 부분 수열의 합 리스트를 정렬 후 반환 
    '''
    result = []

    for i in range(len(seq)+1):
        for comb in combinations(seq, i):
            result.append(sum(comb))
    
    return sorted(result)
    
def solution(N, S, nums):
    answer = 0
    nums_l = nums[:N//2]
    nums_r = nums[N//2:]

    lsub_sum = get_sub_sum(nums_l)
    rsub_sum = get_sub_sum(nums_r)

    # Two Pointer
    l = 0 # lsub_sum의 첫번째
    r = len(rsub_sum) - 1 # rsub_sum의 마지막
    
    while l < len(lsub_sum) and r >= 0:
        nl = l + 1
        nr = r - 1

        # 중복 확인
        while nl < len(lsub_sum) and lsub_sum[nl] == lsub_sum[l]:
            nl += 1
        while nr >= 0 and rsub_sum[nr] == rsub_sum[r]:
            nr -= 1
        
        # S check
        sum_sub = lsub_sum[l] + rsub_sum[r]

        if sum_sub == S:
            answer += (nl - l) * (r - nr)
            l, r = nl, nr

        elif sum_sub < S:
            l = nl

        else: # sum_sub > S
            r = nr
    
    # S == 0일 때, 양 쪽 다 공집합인 경우를 빼준다.
    if S == 0: 
        answer -= 1

    return answer


if __name__ == "__main__":
    N, S = map(int, input().split())
    nums = list(map(int, input().split()))

    print(solution(N, S, nums))