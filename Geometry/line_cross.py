# 백준 #17386 선분 교차 1
'''
    Algorithm: CCW (Counter ClockWise = 선분 교차 판별 알고리즘)
    Time Complexity: O(1)
'''
import sys

input = sys.stdin.readline
INF = sys.maxsize

def solution(L1: tuple, L2: tuple) -> int:
    def separte_point(L: tuple) -> tuple:
        return (L[0], L[1]), (L[2], L[3])

    def CCW(p1: tuple, p2: tuple, p3: tuple) -> int:
        '''
            세 점에 대한 방향성을 나타내는 함수 
            S > 0 : 반시계 방향
            S < 0 : 시계 방향
            S = 0 : 세 점이 평행
        '''
        S = p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] \
            - (p1[0]*p3[1] + p2[0]*p1[1] + p3[0]*p2[1])
        
        return S
    
    # 각 두 선분에 대해 다른 선분의 두 점이 각각 다른 방향을 나타낼 경우 교차
    A, B = separte_point(L1)
    C, D = separte_point(L2)

    if CCW(A,B,C) * CCW(A,B,D) <= 0 and CCW(C,D,A) * CCW(C,D,B) <= 0:
        # 문제에서 세 점이 일직선 위에 있는 경우는 없다고 했으므로 
        # 두 경우 모두 0이 되는 경우는 고려하지 않아도 되겠다.
        return 1

    return 0


if __name__ == "__main__":
    L1 = tuple(map(int, input().split()))
    L2 = tuple(map(int, input().split()))

    print(solution(L1, L2))

# -------------------------------------------------------------------- #
'''
    Algorithm: 기하학, 수학
    Time Complexity: O(1)
'''
import sys

input = sys.stdin.readline
INF = sys.maxsize

def solution(L1: tuple, L2: tuple) -> int:

    def get_gradient(a, b, c, d):
        ''' 두 점을 잇는 선분의 기울기를 구하는 함수 '''
        if a != c:
            return (b-d) / (a-c)
        else:
            return INF

    def get_f(a, b, c, d):
        ''' 두 점을 잇는 직선의 방정식 '''
        if a != c:
            return lambda x: ((b-d)/(a-c)) * (x-a) + b
        else:
            return lambda x: b

    def is_cross(L1: tuple, L2: tuple) -> int:
        ''' 두 선분이 교차하는 지 확인 '''
        a, b, c, d = L1
        e, f, g, h = L2

        m1 = get_gradient(a, b, c, d)
        m2 = get_gradient(e, f, g, h)

        if m1 == m2:
            return 0

        if m1 == INF:
            fx = get_f(e, f, g, h)

        else:
            fx = get_f(a, b, c, d)

        cross_x = (m1*a - m2*e + f - b) / (m1 - m2)
        cross_y = fx(cross_x)
        
        if min(a, c) <= cross_x <= max(a, c) and \
            min(b, d) <= cross_y <= max(b, d) and \
            min(e, g) <= cross_x <= max(e, g) and \
            min(f, h) <= cross_y <= max(f, h):
            return 1
        
        return 0

    return is_cross(L1, L2)


if __name__ == "__main__":
    L1 = tuple(map(int, input().split()))
    L2 = tuple(map(int, input().split()))

    print(solution(L1, L2))