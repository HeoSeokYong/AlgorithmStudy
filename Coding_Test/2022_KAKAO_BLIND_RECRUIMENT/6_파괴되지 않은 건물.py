# 프로그래머스 2022 카카오 공채 #6 파괴되지 않은 건물
'''
    Algorithm: 누적합
    Time Complexity: O(K + N*M) : K = len(skill)
    
    누적합을 이용한 변화량 그래프 
    시작지점에 변량을 저장하고 
    끝나는 지점 다음 값에 -변량을 넣어 뒤가 변하는 것을 막음.
'''

def solution(board, skill):
    answer = 0
    N, M = len(board), len(board[0])
    change = [[0 for _ in range(M+1)] for _ in range(N+1)]
    
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1: # ATTACK
            degree = -degree
            
        change[r1][c1] += degree
        change[r1][c2+1] -= degree
        change[r2+1][c1] -= degree
        change[r2+1][c2+1] += degree

    # change의 누적합 진행
    for i in range(N): # 아래 방향
        for j in range(M):
            change[i+1][j] += change[i][j]

    for j in range(M): # 오른쪽 방향
        for i in range(N):
            change[i][j+1] += change[i][j]
            
    for i in range(N):
        for j in range(M):
            if board[i][j] + change[i][j] > 0:
                answer += 1

    return answer