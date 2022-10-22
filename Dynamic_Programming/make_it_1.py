# 백준 #12852 1로 만들기 2
'''
    알고리즘: dp
'''
import sys
from collections import deque

input = sys.stdin.readline

INF = int(1e6+1)

def solution(N):
    # dp_min = 해당 수 까지 가는 최소 비용
    # past_dict = 해당 수의 이전 수중 가장 dp_min이 작은 값을 저장하는 dict
    dp_min = [INF] * (N+1)
    past_dict = {}
    
    deq = deque([1])
    dp_min[1] = 0
    past_dict[1] = 0

    while deq:
        val = deq.popleft()

        if val == N:
            break

        for i in range(1, 4):
            if i == 1:
                next_val = val + 1
            else:
                next_val = val * i
            
            if 1 <= next_val <= N and dp_min[next_val] > dp_min[val] + 1:
                dp_min[next_val] = dp_min[val] + 1
                past_dict[next_val] = val

                deq.append(next_val)

    print(dp_min[N])
    answer = []
    while N:
        answer.append(N)
        N = past_dict[N]

    print(*answer)


if __name__ == "__main__":
    N = int(input())

    solution(N)
    