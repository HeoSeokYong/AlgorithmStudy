'''
    BOARD => 0: white, 1: red, 2: blue
    DIR => 1: right, 2: left, 3: up, 4: down
'''
import sys

input = sys.stdin.readline
dir = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}

def NewGame2(N, K, board, pieces):
    # board위의 말들을 표시
    piece_on_board = [[[] for _ in range(N)] for _ in range(N)] 
    
    for k in pieces.keys():
        x, y = pieces[k]['loc']
        piece_on_board[x][y].append(k)
    
    turn = 0
    condition = True

    while condition and turn <= 1000:

        for i in range(1, K+1):
            x, y = pieces[i]['loc']
            dx, dy = pieces[i]['dir']

            nx, ny = x + dx, y + dy

            # blue or out of range
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
                pieces[i]['dir'] = (-dx, -dy)
                nx = x - dx
                ny = y - dy

                # Don't move
                if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
                    continue
            
            # Move (White or Red)
            idx = piece_on_board[x][y].index(i)
            P = piece_on_board[x][y][idx:]

            # if red -> Move reverse
            if board[nx][ny] == 1:
                P.reverse()

            for p in P:
                piece_on_board[x][y].remove(p)
                piece_on_board[nx][ny].append(p)
                pieces[p]['loc'] = (nx, ny)
            
            # Quit
            if len(piece_on_board[nx][ny]) >= 4:
                condition = False
                break
            
        turn += 1

    if turn > 1000:
        return -1
    else:
        return turn


if __name__ == "__main__":
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    pieces = {}

    for i in range(K):
        r, c, d = map(int, input().split())
        pieces[i+1] = {'loc': (r-1, c-1), 'dir': dir[d]}

    print(NewGame2(N, K, board, pieces))
