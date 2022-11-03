# # 백준 #2258 정육점
# '''
#     Algorithm: 누적합
#     Time Complexity: O(N)

# '''
# import sys

# input = sys.stdin.readline

# def solution(N, M):
#     meats = [tuple(map(int, input().split())) for _ in range(N)]

#     # 가격 오름차순, 무게 내림차순
#     meats.sort(key=lambda x:(x[1], -x[0]))

#     # 누적 합
#     sum_meats = [meats[0]]
#     cur_cost = meats[0][1]

#     for m, c in meats[1:]:
#         nm = sum_meats[-1][0] + m

#         if cur_cost < c:
#             cur_cost = c
#             sum_meats.append((nm, c))
#         else: # cur_cost == c
#             sum_meats.append((nm, sum_meats[-1][1] + c))
    
#     # 가격 오름차순, 무게 내림차순
#     sum_meats.sort(key=lambda x:(x[1], -x[0]))

#     for m, c in sum_meats:
#         if m >= M:
#             return c

#     return -1


# if __name__ == "__main__":
#     N, M = map(int, input().split())

#     print(solution(N, M))

# ----------------------------------------------------- #
'''
    Algorithm: greedy
    Time Complexity: O(N)

'''
import sys

input = sys.stdin.readline
INF = sys.maxsize

def solution(N, M):
    result = INF
    meats = [tuple(map(int, input().split())) for _ in range(N)]

    # 가격 오름차순, 무게 내림차순
    meats.sort(key=lambda x:(x[1], -x[0]))

    sum_weight = 0
    prev_cost = -1

    for m, c in meats:
        if prev_cost < c:
            prev_cost = c
            same_count = 1

        else: # prev_cost == c
            same_count += 1
        
        sum_weight += m

        if sum_weight >= M:
            
            result = min(result, c * same_count)

    if result == INF:
        return -1
    else:
        return result

if __name__ == "__main__":
    N, M = map(int, input().split())

    print(solution(N, M))