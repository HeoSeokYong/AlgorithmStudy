# 백준 #1027 고층 건물
'''
    Algorithm: 기하학, 수학, 브루트포스
    Time Complexity: O(N^3)

    N <= 50의 자연수이므로 브루트포스가 가능하겠다.
    
    (a,b), (c,d)를 지나는 직선: y = (b-d)/(a-c)(x-1) + b
'''
import sys
from typing import Callable

input = sys.stdin.readline

def solution(N: int) -> int:
    building = list(map(int, input().split()))
    result = [0 for _ in range(N)]

    def get_f(a: int, b: int, c: int, d: int) -> Callable:
        ''' (a,b) (c,d) 를 잇는 직선의 식을 반환 '''
        return lambda x: ((b-d)/(a-c))*(x-a) + b
        
    for i in range(N):
        # left
        for j in range(0, i):
            f = get_f(i, building[i], j, building[j])
            flag = True
            # buliding check (between i, j)
            for k in range(j+1, i):
                if f(k) <= building[k]:
                    flag = False
                    break
            if flag:
                result[i] += 1
        # right
        for j in range(i+1, N):
            f = get_f(i, building[i], j, building[j])
            flag = True
            # buliding check (between i, j)
            for k in range(i+1, j):
                if f(k) <= building[k]:
                    flag = False
                    break
            if flag:
                result[i] += 1
    
    return max(result)


if __name__ == "__main__":
    N = int(input())

    print(solution(N))


# 01/04 풀이 (다시 풀어보기)

'''
    Algorithm: 기하학, 수학, 브루트포스
    Time Complexity: O(N^3)

    이 경우 result의 원소를 더하고 빼는 경우가 위의 풀이보다 많아 시간이 더 소요된다.
    40 ms -> 약 150 ms
'''
import sys
from typing import Callable

input = sys.stdin.readline

def solution(N: int) -> int:
    building = list(map(int, input().split()))
    result = [0 for _ in range(N)]

    def get_function(a: int, b: int, c: int, d: int) -> Callable:
        ''' (a,b) (c,d) 두 점을 지나는 직선의 함수식을 반환 '''
        return lambda x: ((b-d) / (a-c)) * (x-a) + b

    for i in range(N):
        # left
        for j in range(i):
            f = get_function(i, building[i], j, building[j])
            result[i] += 1
            # buliding check (between i, j)
            for k in range(j+1, i):
                if f(k) <= building[k]:
                    result[i] -= 1
                    break

        # right
        for j in range(i+1, N):
            f = get_function(i, building[i], j, building[j])
            result[i] += 1
            # buliding check (between i, j)
            for k in range(i+1, j):
                if f(k) <= building[k]:
                    result[i] -= 1
                    break

    return max(result)


if __name__ == "__main__":
    N = int(input())

    print(solution(N))