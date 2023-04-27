# 백준 #19940 피자 오븐
'''
    Algorithm: greedy
    Time Complexity: O(T) 

    각 H, T, O 버튼이 얼마나 눌릴 지를 구하고 조정해보자.
'''
import sys
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    return N,


def solution(N:int) -> int:
    click = [0, 0, 0, 0, 0] # ADDH, ADDT, MINT, ADDO, MINO
    
    H = N // 60
    T = (N % 60) // 10
    O = N % 10

    if O > 5: 
        # ADDT 1번과 MINO를 누르는게 더 효율적
        T += 1
        O -= 10
    
    if T > 3:
        # ADDH 1번과 MINT를 누르는게 더 효율적
        H += 1
        T -= 6

    # MINT를 눌러야 하고, ADDO를 5번 클릭하는 상황이라면
    # MINT를 한 번 줄이고 MINO를 5번 누르는 것이 더 낫다.
    if T < 0 and O == 5:
        T += 1
        O -= 10

    click[0] = H
    click[(T < 0) + 1] = abs(T)
    click[(O < 0) + 3] = abs(O)
    
    return click


if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        print(*solution(*read_data()))
