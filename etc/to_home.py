# 백준 #1069 집으로
'''
    Algorithm: 조건 분기
    Time Complexity: -

    좌표상이 아니고 직선거리다.

    # 거리가 점프거리보다 큰 경우
        - 점프를 가능한 하고 남는 거리 걷기
        - 점프를 가능한 하고 남는 거리 1번 더 꺾어 뛰기
        - 걷기
    # 거리가 점프거리보다 작은 경우
        - 점프를 한후 지나간 거리 되돌아 오기
        - 2번 꺾어뛰기
        - 걷기
'''
import sys
import math

input = sys.stdin.readline

def solution(X, Y, D, T):
    dist = math.sqrt(X**2 + Y**2)

    # jump
    if dist >= D:
        time = min((dist // D) * T + dist % D, ((dist // D) + 1) * T, dist)

    # no jump
    else:
        time = min(abs(dist-D) + T, 2 * T, dist)

    return time


if __name__ == "__main__":
    X, Y, D, T = map(int, input().split())

    print(solution(X, Y, D, T))