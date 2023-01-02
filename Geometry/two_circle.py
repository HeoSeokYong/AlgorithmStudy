# 백준 #7869 두 원
'''
    Algorithm: 기하학, 수학, 조건 분기
    Time Complexity: O(1)

    1. 두 원이 겹치지 않을 때 --> 0
    2. 한 원이 다른 원에 포함될 때 -> 작은 원의 넓이
    3. 그 외:
        각 원의 겹치는 부분 부채꼴의 넓이 - 삼각형의 넓이를 더해준다.

    소수점 3자리가 무조건이었다..
'''
import sys
import math

input = sys.stdin.readline

def solution(x1: float, y1: float, r1: float, x2: float, y2: float, r2: float) -> float:
    def get_angle(a: float, b: float, c: float) -> float:
        ''' 세 변이 a, b, c인 삼각형의 a와b의 사이각을 라디안으로 반환하는 함수 '''
        return math.acos((a**2 + b**2 - c**2)/(2*a*b))
    
    def get_triangle_area(theta: float, r: float) -> float:
        ''' 반지름이 r이고 그 사이각이 theta인 삼각형의 넓이를 반환 '''
        return (r**2 * math.sin(theta)) / 2

    def get_sector_area(theta: float, r: float) -> float:
        ''' 반지름이 r이고 각이 theta인 부채꼴의 넓이를 반환 '''
        return (r**2 * theta) / 2

    center_line = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))

    if r1 + r2 <= center_line:
        S = float(0)

    elif abs(r2-r1) >= center_line:
        S = math.pi * (min(r1, r2)**2)

    else:
        theta1 = 2 * get_angle(r1, center_line, r2)
        theta2 = 2 * get_angle(r2, center_line, r1)

        S1 = get_sector_area(theta1, r1) - get_triangle_area(theta1, r1)
        S2 = get_sector_area(theta2, r2) - get_triangle_area(theta2, r2)
        S = S1 + S2

    S = str(round(S, 3))
    l = len(S.split('.')[-1])

    while l < 3:
        S += '0'
        l += 1

    return S


if __name__ == "__main__":
    print(solution(*map(float, input().split())))