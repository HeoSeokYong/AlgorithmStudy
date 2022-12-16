# 백준 #5052 전화번호 목록
'''
    Algorithm: 자료 구조
    Time Complexity: O(KN) (K: 문자열의 길이)

'''
import sys
from typing import List

input = sys.stdin.readline

def solution(N: int, pn_list: List[str]) -> str:
    pn_set = set(pn_list)

    for pn in pn_list:
        pn_set.discard(pn)
        tmp = ''
        for s in pn:
            tmp += s
            if tmp in pn_set:
                return 'NO'
        pn_set.add(pn)

    return 'YES'


if __name__ == "__main__":
    T = int(input())

    for test_case in range(T):
        N = int(input())
        pn_list = [input().rstrip() for _ in range(N)]

        print(solution(N, pn_list))

'''
    Algorithm: 정렬
    Time Complexity: O(NlogN)

    정렬을 하면 접두어가 같거나 비슷한 번호끼리 붙어 있겠다.
'''
import sys
from typing import List

input = sys.stdin.readline

def solution(N: int, pn_list: List[str]) -> str:
    pn_list.sort()

    for i in range(N-1):
        if pn_list[i+1].startswith(pn_list[i]):
            return 'NO'

    return 'YES'


if __name__ == "__main__":
    T = int(input())

    for test_case in range(T):
        N = int(input())
        pn_list = [input().rstrip() for _ in range(N)]

        print(solution(N, pn_list))