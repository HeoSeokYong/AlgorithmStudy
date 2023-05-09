# 백준 #17951 흩날리는 시험지 속에서 내 평점이 느껴진거야
'''
    Algorithm: parametric search
    Time Complexity: NlogX (X: 모든 시험지 점수의 합)
    
    최적화 문제: 시험지를 K개의 그룹으로 나눌 때 얻을 수 있는 최대한의 최소점(그룹 점수의 합)은 얼마인가?
    결정 문제: 시험지를 K개의 그룹으로 나눌 때 최소 그룹의 점수를 L 이하로 할 수 있나?
'''
import sys

from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, K = map(int, input().split())
    tests = list(map(int, input().split()))
    return N, K, tests


def solution(N:int, K:int, tests:List[int]) -> int:
    def check(L:int) -> bool:
        num_group, cur_score = 1, 0

        for score in tests:
            cur_score += score

            if cur_score > L:
                cur_score = 0
                num_group += 1
            
            if num_group > K:
                return True
            
        return False
    
    def binary_search(l:int, r:int):
        while l < r:
            if check(mid := (l + r) >> 1):
                l = mid + 1
            else:
                r = mid
        return r

    return binary_search(0, sum(tests))


if __name__ == "__main__":
    print(solution(*read_data()))
