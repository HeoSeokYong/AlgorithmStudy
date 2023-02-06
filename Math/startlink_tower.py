# 백준 #1089 스타트링크 타워
'''
    Algorithm: 구현, 수학
    Time Complexity: O(N)

    꺼져 있는 전구의 일부가 고장 -> 켜져 있는 건 고장 x

    # 1.
    3*5자리를 검사 x (0~9까지) * N개의 숫자를
    => 3*5*10 * N 
    각 자리의 후보들의 평균을 구하고 자릿수를 높여가는 식으로 한다.
    후보들의 평균을 구하는 경우의 수 C : 후보 리스트의 길이
    최악의 경우 => 3 * 5 * 10 * N(10) + C(10) = 1510

    # 2.
    총 15자리를 set를 통해 각 자리가 켜졌을 경우 가능한 숫자들을 저장해보자.
    아주 살짝의 속도 개선이 있다.
'''
import sys
from typing import List, Tuple, Callable

ON, OFF = '#', '.'
nums = [
        "###...#.###.###.#.#.###.###.###.###.###",
        "#.#...#...#...#.#.#.#...#.....#.#.#.#.#",
        "#.#...#.###.###.###.###.###...#.###.###",
        "#.#...#.#.....#...#...#.#.#...#.#.#...#",
        "###...#.###.###...#.###.###...#.###.###"
    ]

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    board = [input() for _ in range(5)]
    return N, board

 
def solution(N:int, board:List[str]) -> float:
    result = 0
    
    def check_num(idx:int) -> List[int]:
        res = []
        # 각 수 n에 대해서 확인
        for n in range(10):
            # 같거나, nums에서 '#'(ON)인 부분이 board에서 '.'(OFF)으로 나타났을 경우
            if all(board[i][4*idx + j] in {nums[i][4*n + j], OFF} for i in range(5) for j in range(3)):
                res.append(n)
        return res

    # main
    for n in range(N):
        # board의 n번째 수를 check
        if cand := check_num(n):
            result *= 10
            result += sum(cand) / len(cand)
        else:
            return -1

    return result


def solution2(N:int, board:List[str]) -> float:
    result = 0
    num_info = [[set() for _ in range(3)] for _ in range(5)]

    def check_num(idx):
        cand = set(range(10))

        for i in range(5):
            for j in range(3):
                if board[i][4*idx + j] == ON:
                    cand &= num_info[i][j]
        return cand

    # main
    for n in range(10):
        for i in range(5):
            for j in range(3):
                if nums[i][4*n + j] == ON:
                    num_info[i][j].add(n)
                    
    for n in range(N):
        if cand := check_num(n):
            result *= 10
            result += sum(cand) / len(cand)
        else:
            return -1
            
    return result


if __name__ == "__main__":
    print(solution(*read_data()))

