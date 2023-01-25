# 백준 #16987 계란으로 계란치기
'''
    Algorithm: brute-force, backtracking
    Time Complexity: -

    - N의 범위가 작으니 brute-force로 하자. (1 <= N <= 8)
'''
import sys
from typing import List, Tuple, Callable

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    eggs = [list(map(int, input().split())) for _ in range(N)]
    return N, eggs


def solution(N: int, eggs: List[List[int]]) -> int:
    result = 0

    def count_broken_egg() -> int:
        return len([x for x in eggs if x[0] <= 0])

    def break_egg(x: int):
        ''' 현재 들고 있는 계란 x로 계란 깨기 '''
        res = 0

        if x == N:
            return count_broken_egg()

        if eggs[x][0] > 0:
            flag = True
            for i in range(N):
                if i != x and eggs[i][0] > 0:
                    flag = False
                    eggs[x][0] -= eggs[i][1]
                    eggs[i][0] -= eggs[x][1]

                    res = max(res, break_egg(x + 1))

                    eggs[x][0] += eggs[i][1]
                    eggs[i][0] += eggs[x][1]
            
            if flag:
                # 더 이상 깰 계란이 없는 경우 end
                return max(res, count_broken_egg())

        else:
            # 들고 있는 계란이 깨졌을 경우 오른쪽의 안 깨진 계란을 든다.
            break_egg(x + 1)
        
        return res

    result = break_egg(0)

    return result


if __name__ == "__main__":
    print(solution(*read_data()))

