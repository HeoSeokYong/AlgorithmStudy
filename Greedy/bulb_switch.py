# 백준 #2138 전구와 스위치
'''
    Algorithm: greedy
    Time Complexity: O(N)

    왼쪽부터 완성시켜보자.
'''
import sys
from typing import Tuple, Callable, List


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    cur_state = list(map(int, list(input())))
    target = list(map(int, list(input())))
    return N, cur_state, target


def solution(N:int, cur_state:List[int], target:List[int]) -> int:
    res_on, res_off = 1, 0 # 첫 스위치를 눌렀을 때, 누르지 않았을 때
    off_state = cur_state.copy()
    
    # 첫 스위치를 눌렀을 때
    cur_state[0] = not cur_state[0]
    cur_state[1] = not cur_state[1]

    for i in range(1, N):
        if cur_state[i-1] != target[i-1]:
            res_on += 1
            for di in [-1, 0, 1]:
                if i+di < N:
                    cur_state[i+di] = not cur_state[i + di]

    # 첫 스위치를 누르지 않았을 때
    for i in range(1, N):
        if off_state[i-1] != target[i-1]:
            res_off += 1
            for di in [-1, 0, 1]:
                if i + di < N:
                    off_state[i+di] = not off_state[i+di]

    if cur_state == target and off_state == target:
        return min(res_on, res_off)
    elif cur_state == target:
        return res_on
    elif off_state == target:
        return res_off

    return -1


if __name__ == "__main__":
    print(solution(*read_data()))
