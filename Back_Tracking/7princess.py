# 백준 #1941 소문난 칠공주
'''
    Algorithm: combination, backtracking, bfs
    Time Complexity: -

    다솜파, 도연파
    1. 7명의 여학생들로 구성되어야 한다.
    2. 7명의 자리는 서로 가로나 세로로 반드시 인접해 있어야 한다.
    3. 반드시 ‘이다솜파’의 학생들로만 구성될 필요는 없다.
    4. 7명의 학생 중 ‘이다솜파’의 학생이 적어도 4명 이상은 반드시 포함되어 있어야 한다.

    모든 경우의 수    
    25개의 학생 중 7명을 뽑는 경우의 수 중에
    다솜파가 4명 이상, 7명이 인접해 있는 지를 확인한다.
'''
import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

def solution(seat: list[str]) -> int:
    combs = combinations([(r, c) for r in range(5) for c in range(5)], 7)
    drdc = ((0, 1), (1, 0), (0, -1), (-1, 0))
    result = 0

    def dasom_gang(students: list[tuple]) -> bool:
        ''' 이다솜파의 학생이 우위인 지 확인하는 함수 '''
        return [seat[r][c] for r, c in students].count('S') >= 4

    def is_adjacent(students: list[tuple]) -> bool:
        ''' 7명의 학생이 인접한 지 확인하는 함수 '''
        q = deque([students[0]]) # bfs

        set_student = set(students)

        while q:
            r, c = q.popleft()

            for dr, dc in drdc:
                nr, nc = r + dr, c + dc

                if 0 <= nr < 5 and 0 <= nc < 5 and (nr, nc) in set_student:
                    set_student.discard((nr, nc))
                    q.append((nr, nc))

        if set_student: # 남은 학생이 있을 경우
            return False
        else:
            return True    

    for students in combs:
        if dasom_gang(students) and is_adjacent(students):
            result += 1

    return result


if __name__ == "__main__":
    seat = [input().rstrip() for _ in range(5)]

    print(solution(seat))


