# 백준 #1484 다이어트
'''
    Algorithm: 수학
    Time Complexity: 

    G = cur^2 - rem^2 = c^2 - r^2 = (c+r)(c-r)
    c,r = 곱해서 G가되는 G의 약수들의 조합일 것이다.
    ex 1) 15 -> 1 3 5 15
    - 1, 15
        c+r = 15, c-r = 1  => c=8,r=7
    - 3, 5
        c+r = 5, c-r = 3  => c=4,r=1

    ex 2) 16 -> 1 2 4 8 16
    - 1, 16
        c+r = 16, c-r = 1  => c=8.5,r=7.5 -> 자연수 확인 필요
    - 2, 8
        c+r = 8, c-r = 2 -> c=5,r=3
    - 4
        c+r = 4, c-r = 4  => c=4, r=0  -> 자연수 확인 필요
'''
import sys

input = sys.stdin.readline

def solution(G: int) -> list[int]:
    result = []

    def check_weight(a: int, b: int) -> int:
        # a <= b
        cur = (a+b) / 2
        rem = b - cur

        if cur != 0 and cur.is_integer() and rem != 0:
            return cur

        return 0

    # 약수 구하기
    for i in range(1, int(G**(1/2)) + 1):
        if G % i == 0:
            weight = check_weight(i, G // i)
            if weight:
                result.append(int(weight))

    if result:
        return sorted(result)
    
    return [-1]


if __name__ == "__main__":
    G = int(input())

    print(*solution(G), sep='\n')