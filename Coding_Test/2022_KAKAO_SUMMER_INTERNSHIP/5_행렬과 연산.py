# 프로그래머스 2022 카카오 채용연계형 여름 인턴십 #5 행렬과 연산
'''
    알고리즘: 구현
    행렬에 접근할 때, 선형 연산 안하게 주의
    행렬을 나눠서 하는 것으로 생각해보기.
    효율성 2,4 시간초과
# '''
# from collections import deque

# def solution(rc, operations):
#     result = deque([deque(x) for x in rc])
#     row, col = len(result), len(result[0])
#     len_round = 2 * row + 2 * col - 4
    
#     def ShiftRow(cnt):
#         key = True
#         cnt %= row

#         # 절반을 기준으로 방향을 정함
#         if cnt > row // 2:
#             cnt = row - cnt
#             key = False

#         for _ in range(cnt):
#             if key:
#                 result.rotate()
#             else:
#                 result.rotate(-1)
    
#     def Rotate(cnt):
#         key = True
#         # 한바퀴 도는 경우
#         cnt %= len_round

#         if cnt == 0:
#             return result
        
#         # 둘레의 절반보다 크면 방향을 반대로
#         if cnt > len_round // 2:
#             cnt = len_round - cnt
#             key = False
        
#         i, idx = 0, 0

#         if key:
#             ''' 행렬의 바깥쪽에 있는 원소들을 시계 방향으로 회전시킵니다. '''
#             while idx < row-1:
#                 result[idx].appendleft(result[i+1].popleft())
#                 result[-1-idx].append(result[-2-i].pop())

#                 cnt -= 1

#                 if cnt <= 0:
#                     idx += 1
                
#                 if i < row-2:
#                     i += 1

#         else:
#             ''' 행렬의 바깥쪽에 있는 원소들을 시계 반대 방향으로 회전시킵니다. '''
#             while idx < row-1:
#                 result[idx].append(result[i+1].pop())
#                 result[-1-idx].appendleft(result[-2-i].popleft())

#                 cnt -= 1

#                 if cnt <= 0:
#                     idx += 1
                
#                 if i < row-2:
#                     i += 1

#     def get_duplicate_oper(operations):
#         ''' 연속적인 같은 operation을 개수와 명령으로 묶은 리스트를 반환'''
#         shift_cnt, rotate_cnt = 0, 0
#         dup_op = []
#         operations.append("finish")

#         for op in operations:
#             if op == 'ShiftRow':
#                 shift_cnt += 1
#                 if rotate_cnt > 0:
#                     dup_op.append((rotate_cnt, "Rotate"))
#                     rotate_cnt = 0
#             elif op == "Rotate":
#                 rotate_cnt += 1
#                 if shift_cnt > 0:
#                     dup_op.append((shift_cnt, "ShiftRow"))
#                     shift_cnt = 0
#             else: # final
#                 if rotate_cnt > 0:
#                     dup_op.append((rotate_cnt, "Rotate"))
#                 if shift_cnt > 0:
#                     dup_op.append((shift_cnt, "ShiftRow"))
                    
#         return dup_op
        
#     operations = get_duplicate_oper(operations)
        
#     for cnt, op in operations:
#         if op == 'ShiftRow':
#             ShiftRow(cnt)

#         elif op == 'Rotate':
#             Rotate(cnt)

#     return [list(x) for x in result]
'''
    행렬을 나눠 움직이는데 드는 비용을 많이 줄였다
'''
from collections import deque

def solution(rc, operations):
    # 첫번째 열, 마지막 열, 그리고 중간의 행들을 따로 관리한다.
    row, col = len(rc), len(rc[0])
    col_left = deque()
    col_right = deque()
    center = deque()
    
    for i in range(row):
        tmp = deque()
        for j in range(col):
            if j == 0:
                col_left.append(rc[i][j])
            elif j == col-1:
                col_right.append(rc[i][j])
            else:
                tmp.append(rc[i][j])
        center.append(tmp)
    
    def ShiftRow():
        # 각 덱의 마지막 원소를 맨 앞으로 한다.
        center.rotate()
        col_left.rotate()
        col_right.rotate()

    def Rotate():
        # col_left, col_right, center[0], center[-1] 만 움직이면 된다.
        if col == 2: # no center
            col_left.append(col_right.pop())
            col_right.appendleft(col_left.popleft())
        else:
            col_left.append(center[-1].popleft())
            col_right.appendleft(center[0].pop())
            center[0].appendleft(col_left.popleft())
            center[-1].append(col_right.pop())

    for op in operations:
        if op == 'ShiftRow':
            ShiftRow()
        elif op == 'Rotate':
            Rotate()

    answer = []
    # 최종 행렬 만들기
    for i in range(row):
        tmp = []
        for j in range(col):
            if j == 0:
                tmp.append(col_left[i])
            elif j == col-1:
                tmp.append(col_right[i])
            else:
                tmp.append(center[i][j-1])

        answer.append(tmp)

    return answer

if __name__ == "__main__":
    cases = []
    cases.append([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]])
    cases.append([[[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]])
    cases.append([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]])
    cases.append([[[1,2], [3,4]], ["Rotate", "Rotate"]])
    cases.append([[[2,1,2,3], [3,4,5,4]],['Rotate']*5])
    cases.append([[[1,2],[2,3],[3,4],[4,5]], ["Rotate"]*8])
    # cases.append([[[1]*50000 for _ in range(50000)], ["Rotate"] * 100000])

    for a, b in cases:
        for x in solution(a, b):
            print(x)
        print()