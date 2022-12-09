# 백준 #11054 가장 긴 바이토닉 부분 수열
'''
    Algorithm: dp, binary_search, LIS
    Time Complexity: O(NlogN)

    1번째 수부터 시작하는 LIS와 마지막 수부터 시작하는 LIS로 
    각 위치 별 증가하고 감소하는 최대 길이를 구한다.
    그 합이 가장 큰 경우 가장 긴 바이토닉 수열이다.
'''
import sys

input = sys.stdin.readline

def solution(N: int, A: list[int]) -> int:
    dp = [[0, 0] for _ in range(N)]
    seq_in = [A[0]]
    seq_de = [A[-1]]

    def binary_search(l: int, r: int, val: int, seq: list[int]) -> int:
        while l < r:
            mid = (l+r) // 2
            
            if seq[mid] < val:
                l = mid + 1
            else:
                r = mid

        return r

    def bitonic(seq: list[int], i: int, x: int) -> None:
        if seq[-1] < A[i]:
            seq.append(A[i])
            dp[i][x] = len(seq) - 1
        else:
            dp[i][x] = binary_search(0, len(seq), A[i], seq)
            seq[dp[i][x]] = A[i]


    for i in range(1, N):
        bitonic(seq_in, i, 0)
        bitonic(seq_de, N-i-1, 1)
    
    return max([sum(x) for x in dp]) + 1


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))

    print(solution(N, A))