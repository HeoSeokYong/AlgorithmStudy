# 백준 #13397 구간 나누기 2
'''
    Algorithm: parametric search
    Time Complexity: NlogD (D: 배열 최댓값과 최솟값의 차이)

    최적화 문제 Q. 그룹을 M 이하의 개수로 나눌때 얻을 수 있는 최소한의 점수(최댓값-최솟값)는 얼마인가?
    결정 문제 -> 그룹을 M 이하의 개수로 나눌 때 최대 그룹의 점수를 L 이하로 할 수 있나?
    L의 범위: (최소: 자기자신=0) <= L <= (전체 배열의 최댓값-최솟값)
'''
import sys
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip() 


def read_data() -> Tuple:
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    return N, M, array


def solution(N:int, M:int, array:List[int]) -> int:
    def check(L:int) -> bool:
        res = 1
        max_num, min_num = 0, float('inf')

        for num in array:
            max_num = max(max_num, num)
            min_num = min(min_num, num)
            
            if max_num - min_num > L:
                max_num, min_num = num, num
                res += 1
            
            if res > M:
                return True

        return False
    
    def binary_search(l:int, r:int) -> int:
        while l < r:
            if check(mid := (l + r) >> 1):
                l = mid + 1
            else:
                r = mid
        return r

    return binary_search(0, max(array) - min(array))


if __name__ == "__main__":
    print(solution(*read_data()))
