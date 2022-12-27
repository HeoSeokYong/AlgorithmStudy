# 백준 #24462 일어나... 코딩해야지...
'''
    Algorithm: 구현, 수학
    Time Complexity: O(N^2)

    (시작 시간, 스누즈 시간, 알람이 총 울린 횟수)
'''
import sys
import math

input = sys.stdin.readline

def solution(N: int, D: int) -> int:
    snooze = []
    max_num = 0
    alarm = (0, 0)

    for _ in range(N):
        t, k = map(int, input().split())
        num = (D // k) + 1 - (t // k)
        snooze.append((t, k, num))

    # 모든 경우의 수 비교
    for i in range(N):
        t1, k1, n1 = snooze[i]
        for j in range(i+1, N):
            t2, k2, n2 = snooze[j]

            # 최소공배수
            LCM = math.lcm(k1, k2) 

            # 두 알람이 울리는 횟수 - 겹치는 최소공배수의 개수
            num = n1 + n2
            num -= (D // LCM) + 1 - math.ceil(max(t1, t2) / LCM)

            # 갱신
            if max_num <= num:
                if max_num < num or alarm > (i+1, j+1):
                    alarm = (i+1, j+1)
                max_num = num

    print(*alarm)
    return max_num


if __name__ == "__main__":
    N, D = map(int, input().split())

    print(solution(N, D))


