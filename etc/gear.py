# 백준 #14891 톱니바퀴
'''
    Algorithm: 덱, 구현
    Time Complexity: O(N^2*K) => N: 톱니바퀴의 개수 

'''
import sys
from typing import List
from collections import deque

input = sys.stdin.readline

N, S = 0, 1
CLOCKWISE, COUNTER_CLOCKWISE = 1, -1
RIGHT_GEAR, LEFT_GEAR = 2, 6 

def solution(gear: List[deque], K: int) -> int:

    def rotate(x: int, d: int):
        rotate_gear = deque([(x, d)])

        # right check
        for i in range(x+1, 4):
            idx, dir_ = rotate_gear[-1]
            if gear[idx][RIGHT_GEAR] != gear[i][LEFT_GEAR]:
                rotate_gear.append((i, -dir_))
            else:
                break
        
        # left check
        for i in range(x-1, -1, -1):
            idx, dir_ = rotate_gear[0]
            if gear[idx][LEFT_GEAR] != gear[i][RIGHT_GEAR]:
                rotate_gear.appendleft((i, -dir_))
            else:
                break
        
        for idx, dir_ in rotate_gear:
            if dir_ == CLOCKWISE:
                gear[idx].rotate()
            elif dir_ == COUNTER_CLOCKWISE:
                gear[idx].rotate(-1)

    def get_score() -> int:
        score = 0

        for i in range(4):
            if gear[i][0] == S:
                score += 2**i

        return score

    for _ in range(K):
        idx, dir_ = map(int, input().split())

        rotate(idx-1, dir_)

    return get_score()


if __name__ == "__main__":
    gear = [deque(map(int, list(input().rstrip()))) for _ in range(4)]
    K = int(input())

    print(solution(gear, K))