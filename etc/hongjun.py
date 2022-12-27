# 백준 #1222 홍준 프로그래밍 대회
'''
    Algorithm: 수학
    Time Complexity: O(N + S) (S: 아래 try2 설명)

    try 1) 약수 활용 : 시간 초과
        모든 수의 약수를 구함 => Nsqrt(N) (2 <= N <= 200000)
        약수의 개수를 카운트 하고 (약수의 범위는 1~2000000)
        나온 모든 약수를 검사 O(D) (D: 약수의 개수)
        => N*sqrt(N) + D => 최대 9000만 정도? 

    try 2) 배수 활용 : 이게 되네?
        약수의 범위 (1 <= C: max(학생 수) <= 2000000)
        모든 약수에 대해 배수가 되는 학생 수를 가진 학교를 카운트
        경우의 수는 처음 학교의 학생 수를 카운트 하는 N
        모든 약수에 대해 탐색하는 경우는,
        k가 1부터 C까지 C/k를 더하면 되겠다.
        S : sum_{k=1}^{C} C/k => C가 최대일 때 약 30171747 => 2초 제한 안에 나온다!
'''
import sys
from typing import List

input = sys.stdin.readline

def solution(N: int, students: List[int]) -> int:
    result = 0
    MAXD = max(students)
    participant = [0 for _ in range(MAXD + 1)]

    for stud in students:
        participant[stud] += 1
      
    for i in range(1, MAXD + 1): # i: 팀원의 수
        cnt = 0
        # 학생의 수가 i에 배수인 경우를 cnt에 카운트
        for j in range(1, MAXD // i + 1):
            cnt += participant[i*j] 

        if cnt >= 2: # 참가팀이 2팀 이상인 경우
            result = max(result, i * cnt)

    return result


if __name__ == "__main__":
    N = int(input())
    students = list(map(int, input().split()))

    print(solution(N, students))