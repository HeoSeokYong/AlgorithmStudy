# 백준 #15927 회문은 회문아니야!!
'''
    Algorithm: 조건 분기
    Time Complexity: O(N) (N: 문자열의 길이)

    1. 문자열이 palindrome인 경우,
        1-1. 모두 같은 문자인 경우, 
            => -1 리턴 (회문이 아닌 경우가 없음)
        1-2. 모두 같은 문자가 아닌 경우,
            => N - 1 리턴 (1자리만 빼도 palindrome이 아니게 됨)
    2. 문자열이 palindrome이 아닌 경우,
        => N 리턴
'''
import sys

input = sys.stdin.readline

def solution(S: str) -> int:

    def is_palindrome(s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    
    if is_palindrome(S):
        if len(set(S)) == 1:
            return -1
        else:
            return len(S)-1
    
    return len(S)


if __name__ == "__main__":
    S = input().rstrip()

    print(solution(S))