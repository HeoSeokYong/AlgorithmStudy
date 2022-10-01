'''
    vector: 도착 점 - 출발 점
    벡터의 합: 도착 점들의 합 - 출발 점들의 합
    brute-force 로 해보자 -> combination
    모든 점들의 (x축 합, y축 합) = (출발 x축 + 도착 x축, 출발 y축 + 도착 y축)
'''

import sys
import math
from itertools import combinations

input = sys.stdin.readline
INF = sys.maxsize

def get_vector_size(start, end):
    return math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)

def sum_vector_list(vector_list):
    x_sum, y_sum = 0, 0
    for vector in vector_list:
        x_sum += vector[0]
        y_sum += vector[1]

    return (x_sum, y_sum)

def minus_vector(v1, v2):
    return (v1[0]-v2[0], v1[1]-v2[1])

def solution(N, dots):
    answer = INF
    # 모든 점들의 합
    dots_sum = sum_vector_list(dots)

    # 가능한 모든 도착점들의 집합
    for ends in combinations(dots, N//2):
        ends_sum = sum_vector_list(ends)
        starts_sum = minus_vector(dots_sum, ends_sum)
        
        vector_sum = get_vector_size(starts_sum, ends_sum)
        answer = min(answer, vector_sum)

    return answer


if __name__ == "__main__":
    T = int(input())

    for testcase in range(T):
        N = int(input())
        dots = [tuple(map(int, input().split())) for _ in range(N)]

        print(solution(N, dots))
