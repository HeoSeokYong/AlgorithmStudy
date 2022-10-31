# 백준 #1561 놀이 공원
'''
    Algorithm: binary search
    Time Complexity: O(MlogN)
    
    N 최대 20억, M 최대 1만 -> 이분탐색 필요
    1. 아이들이 모두 탔을 때의 시간을 구함.
    2. 마지막 시간에 탄 아이들을 제외하고 놀이기구를 탄 모든 학생의 수를 구하고
    3. 마지막 시간에 탈 수 있는 아이들을 작은 순서대로 확인하여 N이 될 때 리턴
'''
import sys

input = sys.stdin.readline
MAX_TIME = 2000000000 * 30

def solution(N, M):
    rides = list(map(int, input().split()))

    if N <= M:
        return N

    def check(time):
        ''' 해당 시간동안 태울 수 있는 아이들 수 체크 '''
        res = M
        for ride in rides:
            res += (time-1) // ride
        
        return res < N

    def binary_search(l, r):
        ''' N명의 학생들이 다 탈때까지 걸리는 시간 리턴 '''
        while l < r:
            mid = (l + r) // 2

            if check(mid):
                l = mid + 1
            else:
                r = mid

        return r

    total_time = binary_search(1, MAX_TIME)
    student = 0

    for i in range(M):
        student += total_time // rides[i]
        
        if rides[i] == 1:
            # 마지막 검사 때 비용 1의 놀이기구를 고려하기 위해 1을 빼준다.
            student -= 1

        if total_time % rides[i] > 1:
            student += 1
            
    for i in range(M):
        if total_time % rides[i] == 1 or rides[i] == 1:
            student += 1
            
            if student == N:
                return i + 1


if __name__ == "__main__":
    N, M = map(int, input().split())

    print(solution(N, M))