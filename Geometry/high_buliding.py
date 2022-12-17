# 백준 #1027 고층 건물
'''
    Algorithm: 기하학, 수학, 브루트포스
    Time Complexity: O(N^3)

    N <= 50의 자연수이므로 브루트포스가 가능하겠다.
    
    (a,b), (c,d)를 지나는 직선: y = (b-d)/(a-c)(x-1) + b
'''
import sys

input = sys.stdin.readline

def solution(N: int) -> int:
    building = list(map(int, input().split()))
    result = [0 for _ in range(N)]

    def get_f(a, b, c, d):
        return lambda x: ((b-d)/(a-c))*(x-a) + b
        
    for i in range(N):
        # 왼쪽
        for j in range(0, i):
            # 두 빌딩을 잇는 직선의 방정식
            f = get_f(i, building[i], j, building[j])
            flag = True
            for k in range(j+1, i):
                # 두 빌딩을 잇는 직선이 빌딩을 접하거나 지날 경우
                if f(k) <= building[k]:
                    flag = False
                    break
            if flag:
                result[i] += 1
        # 오른쪽
        for j in range(i+1, N):
            f = get_f(i, building[i], j, building[j])
            flag = True
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