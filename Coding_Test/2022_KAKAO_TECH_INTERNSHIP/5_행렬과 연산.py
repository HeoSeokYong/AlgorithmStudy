'''
    알고리즘: 구현
    행렬에 접근할 때, 선형 연산 안하게 주의
    효율성 1,2,4,6 시간초과
'''
from collections import deque

def solution(rc, operations):
    result = deque([deque(x) for x in rc])
    
    for op in operations:
        if op == 'ShiftRow':
            result.rotate()
            # result.appendleft(result.pop())

        elif op == 'Rotate':
            ''' 행렬의 바깥쪽에 있는 원소들을 시계 방향으로 한 칸 회전시킵니다. '''
            for i in range(len(result)-1):
                # left side
                result[i].appendleft(result[i+1].popleft())

                # right side
                result[-1-i].append(result[-2-i].pop())

    return [list(x) for x in result]


if __name__ == "__main__":
    cases = []
    cases.append([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]])
    cases.append([[[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]])
    cases.append([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]])
    cases.append([[[1,2], [3,4]], ["Rotate", "Rotate"]])
    for a, b in cases:
        for x in solution(a, b):
            print(x)
        print()