# 백준 #1188 음식 평론가
'''
    Algorithm: 정수론
    Time Complexity: O(logN)
    
    소시지 N개를 평론가 M명에게 나눠줘야 한다.
    소시지 N개를 일자로 쭉 붙인 후 잘라서 나눠줌 -> 각 평론가가 받을 소시지의 양은 N/M 개.

    소세지의 처음 부분부터 N/M의 길이만큼 칼질을 한다고 하자.
    ex) N=6, M=9
        6/9, 12/9, 18/9 ... 48/9 => 이렇게 칼질을 하면 6/9의 크기인 소시지 9개가 나오게 된다.
        위를 보면 분자가 분모에 나누어 떨어지는 경우가 있다. => 소시지를 붙인 부분

        (수식)
        kN/M (k는 1 ~ M 까지) N, M의 gcd를 g라고 할때 (N=ng, M=mg)
        kng/mg = kn/m (n과 m은 서로소)
        kn/m이 자연수가 나오려면(소시지를 붙인 부분) k가 m의 배수여야 한다.
        1부터 M까지의 범위에서 M을 g로 나눈 값인 m의 배수가 나오는 경우는 g번이다.(m*g = M 이므로)
        
        따라서 N개의 소시지를 M개로 나누기 위한 칼질 중 g번은 이미 잘려 있으므로 
        총 M - g번 칼질이 필요하다.
'''
import sys
import math
from typing import Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, M = map(int, input().split())
    return N, M


def solution(N:int, M:int) -> int:
    return M - math.gcd(N, M)


if __name__ == "__main__":
    print(solution(*read_data()))
