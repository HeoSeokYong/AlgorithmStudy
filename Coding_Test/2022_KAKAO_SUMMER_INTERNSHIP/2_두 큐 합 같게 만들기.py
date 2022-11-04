# 프로그래머스 2022 카카오 채용연계형 여름 인턴십 #2 두 큐 합 같게 만들기
from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    
    # 두 큐의 합이 홀수인 경우 같아질 수 없음.
    if (s1+s2) % 2:
        return -1

    # 최대 반복 제한을 큐의 4배 길이로 함: 최대 경우의 수는 양쪽 큐를 왕복하는 것(2x2)이라고 생각해서 4배로 했습니다.
    for i in range(len(queue1) * 4):
        if s1 == s2:
            return i
        
        if s1 > s2:
            p = q1.popleft()
            q2.append(p)
            p = -p
        else:
            p = q2.popleft()
            q1.append(p)
            
        s1 += p
        s2 -= p
            
    return -1