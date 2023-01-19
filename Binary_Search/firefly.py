# 백준 #3020 개똥벌레
'''
    Algorithm: 이분 탐색
    Time Complexity: O((N+H)logN)

    석순, 종유석을 별개의 리스트로 입력 후 정렬. -> (NlogN)
    그 후 장애물의 높이 1~H 까지 각 석순, 종유석 별로 이분탐색으로 부딪히는 위치를 찾는다. -> (HlogN)
    정렬을 했기 때문에 부딪히는 인덱스 뒤는 전부 부딪힌다고 볼 수 있다.
    - 높이 별 부딪히는 장애물 개수 
    => ((N//2) - 석순 인덱스) + ((N//2) - 종유석 인덱스) 
        = N - (석순 인덱스 + 종유석 인덱스)
'''
import sys
from typing import Tuple, Callable

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, H = map(int, input().split())

    return N, H


def solution(N: int, H: int) -> Tuple:
    result = [float('inf'), 0] # 장애물의 최솟값, 구간의 수
    stalactite, stalagmite = [], [] # 종유석, 석순

    def binary_search(l: int, r: int, value: int):
        ''' 석순, 종유석의 처음 부딪히는 위치를 찾아 반환 '''
        l1, r1, l2, r2 = l, r, l, r
        # 석순
        while l1 < r1:
            mid = (l1 + r1) >> 1

            if stalagmite[mid] < value:
                l1 = mid+1
            else:
                r1 = mid
        # 종유석
        while l2 < r2:
            mid = (l2 + r2) >> 1
        
            if stalactite[mid] < H - value + 1:
                l2 = mid + 1
            else:
                r2 = mid
        
        return r1, r2

    # main
    for _ in range(N//2):
        stalagmite.append(int(input()))
        stalactite.append(int(input()))

    stalagmite.sort()
    stalactite.sort()

    # 높이 별 부딪히는 장애물 개수 확인
    for h in range(1, H+1):
        num_obstacle = N - sum(binary_search(0, N // 2, h))

        if result[0] > num_obstacle:
            result[0] = num_obstacle
            result[1] = 1

        elif result[0] == num_obstacle:
            result[1] += 1
        
    return result 


if __name__ == "__main__":
    print(*solution(*read_data()))