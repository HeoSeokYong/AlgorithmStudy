# 백준 #2457 공주님의 정원
'''
    3.1 ~ 11.30 까지 꽃의 범위에 맞게 dp로 갱신 후
    11.30 날짜의 dp 값을 확인한다. 
    알고리즘: DP
    시간복잡도: O(NlogN + 270*N) = 약 2800만
'''
import sys

input = sys.stdin.readline
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 각 월별 일수

# 1년 중 3월 1일과 11월 30일의 인덱스
day3_1 = 60 
day11_30 = 334

def get_days(m1, d1, m2, d2):
    ''' 두 날짜의 일 수를 반환 '''
    day1, day2 = d1, d2

    for i in range(1, m1):
        day1 += months[i]

    for i in range(1, m2):
        day2 += months[i]
    
    return day1, day2

# def solution(N, dates):
#     # 순서대로 앞부터 채우기 위해 정렬
#     dates.sort()

#     # dp 행렬
#     year = [0] * 366

#     for date in dates:
#         m1, d1, m2, d2 = date

#         # 3.1 ~ 11.30 만 고려함.
#         if m2 < 3 or m1 > 11: 
#             continue

#         day1, day2 = get_days(m1, d1, m2, d2)

#         day1 = max(day1, day3_1)
#         day2 = min(day2, day11_30+1)

#         val = year[day1-1] + 1

#         # 시작 날짜가 3월 1일보다 크지만(3월 2일 이상) val 이 1일 경우
#         # 즉, 3.1 ~ 11.30 동안 커버하지 못하는 부분이 있는 경우 0을 반환
#         if day1 > day3_1 and val == 1:
#             return 0

#         for i in range(day1, day2):
#             if year[i] == 0:
#                 year[i] = val
#             else:
#                 year[i] = min(year[i], val)

#     return year[day11_30]


# if __name__ == "__main__":
#     N = int(input())
#     date = [tuple(map(int, input().split())) for _ in range(N)]

#     print(solution(N, date))

'''
    알고리즘: 그리디
    시간복잡도: O(NlogN)
'''
import heapq

def solution(N, dates):
    flowers = []

    for date in dates:
        m1, d1, m2, d2 = date

        if m2 < 3 or m1 > 11:
            continue
        
        day1, day2 = get_days(m1, d1, m2, d2)

        day1 = max(day1, day3_1)
        day2 = min(day2, day11_30+1)

        # 빨리 피는 순으로 정렬
        heapq.heappush(flowers, (day1, day2))
    
    stack = []
    while flowers:
        start, end = heapq.heappop(flowers)
        if stack:
            # 현재 가장 늦게 지는 꽃보다 피는 날이 느릴 경우
            if stack[-1][1] < start:
                return 0

            # 이전 것보다 지는 경우가 빠를 경우 pass
            if end <= stack[-1][1]:
                continue

            # 피는 날이 같을 경우 뒤의 꽃이 지는 날짜가 길기 때문에 이전 꽃을 pop
            if stack[-1][0] == start:
                stack.pop()

            # 
            while len(stack) > 1 and stack[-2][1] >= start:
                stack.pop()

        stack.append((start, end))
    
    # 범위를 만족 못했을 경우
    if stack[0][0] > day3_1 or stack[-1][1] <= day11_30:
        return 0
        
    return len(stack)

if __name__ == "__main__":
    N = int(input())
    date = [tuple(map(int, input().split())) for _ in range(N)]

    print(solution(N, date))
