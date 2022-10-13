# 백준 #20061 모노미노도미노 2
'''
    알고리즘: 구현
'''
import sys

input = sys.stdin.readline

def solution(N, blocks):
    '''
        blue와 green board로 구분하여 생각
        둘 다 6x4 의 행렬로 가정하여 품
        blue의 경우 y=x 대칭 시켜 4x6 -> 6x4로 함.
        블록의 형태 - t==1 : 1x1, t==2 : 1x2, t==3 : 2x1
    '''
    total_score = 0

    blue_board = [[0] * 4 for _ in range(6)]
    green_board = [[0] * 4 for _ in range(6)]

    def block_move(board, t, y):
        ''' board에서 블록을 이동 (열 정보만 필요)'''
        idx = 2
        while idx < 6:
            if board[idx][y] or (t == 2 and board[idx][y+1]):
                break
            idx += 1

        board[idx-1][y] = 1
        if t == 2:
            board[idx-1][y+1] = 1
        elif t == 3:
            board[idx-2][y] = 1

    def block_crash(board):
        ''' 행이 타일로 가득찬 경우 score '''
        score = 0

        for i in range(2, 6):
            if 0 not in board[i]:
                del board[i]
                board = [[0, 0, 0, 0]] + board
                score += 1

        return score, board
    
    def check_line(board):
        ''' green과 blue의 0,1 row에 블록이 있을 경우 그만큼 내린다'''
        for _ in range(2):
            if 1 in board[1]:
                del board[-1]
                board = [[0, 0, 0, 0]] + board
        
        return board

    def check_remain(green_board, blue_board):
        ''' 보드에 남은 블록의 수를 리턴 '''
        remain = 0
        for i in range(2, 6):
            remain += sum(green_board[i])
            remain += sum(blue_board[i])
        
        return remain

    def for_blue(t):
        ''' blue는 y=x 대칭 했기 때문에 블록도 y=x 대칭 형태가 됨 '''
        return [1, 3, 2][t-1]

    for t, x, y in blocks:
        # Move
        block_move(green_board, t, y)
        block_move(blue_board, for_blue(t), x) # y=x 대칭이기 때문에 x값을 넣어줌
        
        # Score
        gscore, green_board = block_crash(green_board)
        bscore, blue_board = block_crash(blue_board)
    
        # Line over check
        green_board = check_line(green_board)
        blue_board = check_line(blue_board)

        total_score += (bscore + gscore) 

    return total_score, check_remain(green_board, blue_board)


if __name__ == "__main__":
    N = int(input())
    blocks = [tuple(map(int, input().split())) for _ in range(N)]

    print(*solution(N, blocks), sep='\n')