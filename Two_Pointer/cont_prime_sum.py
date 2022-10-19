# # 백준 #1644 소수의 연속합
'''
    알고리즘: 투포인터
    시간복잡도: O(NlogN) ?? -> 1452 ms
'''
import sys

input = sys.stdin.readline

# 에라토스테네스의 체
def get_prime(x):
    ''' 에라토스테네스의 체를 사용해 x 이하의 소수 리스트를 구함 '''
    prime_list = []
    disc = [False, False] + [True]*(x-1)

    for i in range(2, x+1):
        if disc[i]:
            prime_list.append(i)
            for j in range(2*i, x+1, i):
                disc[j] = False
    
    return prime_list

def solution(N):
    ''' deq을 활용해 연속된 소수들의 합을 확인 '''
    num_cases, s, e = 0, 0, 0
    prime_list = get_prime(N)

    sum_prime = 0
    
    while e < len(prime_list):
        if sum_prime < N:
            if sum_prime + prime_list[e] <= N:
                sum_prime += prime_list[e]
                e += 1
            else:
                sum_prime -= prime_list[s]
                s += 1

        if sum_prime == N:
            num_cases += 1
            sum_prime -= prime_list[s]
            s += 1

    return num_cases


if __name__ == "__main__":
    N = int(input())
    
    print(solution(N))

# -------------------------------------------------------------------- #

'''
    알고리즘: 덱을 활용한 투포인터?
    시간복잡도: O(NlogN) ?? -> 1224 ms
'''
import sys
from collections import deque

input = sys.stdin.readline

# 에라토스테네스의 체
def get_prime(x):
    ''' 에라토스테네스의 체를 사용해 x 이하의 소수 덱을 구함 '''
    prime_deq = deque()
    disc = [False, False] + [True]*(x-1)

    for i in range(2, x+1):
        if disc[i]:
            prime_deq.append(i)
            for j in range(2*i, x+1, i):
                disc[j] = False
    
    return prime_deq

def solution(N):
    ''' deq을 활용해 연속된 소수들의 합을 확인 '''
    num_cases, sum_deq = 0, 0
    prime_deq = get_prime(N)

    deq = deque()
    
    while prime_deq:
        if deq:
            if sum_deq + prime_deq[0] <= N:
                value = prime_deq.popleft()
                deq.append(value)
                sum_deq += value
            
            else:
                sum_deq -= deq.popleft()
        else:
            deq.append(prime_deq.popleft())
            sum_deq = deq[0]
        
        if sum_deq == N:
                num_cases += 1
                sum_deq -= deq.popleft()
                continue

    return num_cases


if __name__ == "__main__":
    N = int(input())

    print(solution(N))