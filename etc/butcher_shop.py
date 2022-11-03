# 백준 #2258 정육점
'''
    Algorithm: 누적합
    Time Complexity:

'''
import sys

input = sys.stdin.readline
INF = sys.maxsize

def solution(N, M):
    meats = [tuple(map(int, input().split())) for _ in range(N)]
    
    if sum(m[0] for m in meats) < M:
        return -1

    # 가격 오름차순, 무게 내림차순
    meats.sort(key=lambda x:(x[1], -x[0]))

    # 누적 합
    sum_meats = [meats[0]]
    cur_cost = meats[0][1]
    for m, c in meats[1:]:
        nm = sum_meats[-1][0] + m
        if cur_cost < c:
            cur_cost = c
            sum_meats.append((nm, c))
        else:
            sum_meats.append((nm, sum_meats[-1][1] + c))
    
    sum_meats.sort(key=lambda x:(x[1], -x[0]))
    print(sum_meats)
    for m, c in sum_meats:
        if m >= M:
            return c

    return -1


if __name__ == "__main__":
    N, M = map(int, input().split())

    print(solution(N, M))