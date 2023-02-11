# 프로그래머스 2022 KAKAO BLIND RECRUITMENT #7 사라지는 발판
'''
    Algorithm: 완전탐색
    Time Complexity: -
    
    재귀 함수를 통한 구현
    
'''
def solution(board, aloc, bloc):
    answer = 0
    R, C = len(board), len(board[0])
    dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    location = [tuple(aloc), tuple(bloc)] # 0: A, 1: B

    def game(move):
        ''' 현재 플레이어가 질 수 있는 경우 True, 아닐 경우 False 와 그 때의 총 이동거리를 반환'''
        nonlocal answer
        
        player = move % 2
        x, y = location[player]
        
        # 현재 플레이어가 밟고 있는 보드가 다른 플레이어에 의해 사라진 경우
        if board[x][y] == 0:
            return True, move
            
        match_result = [] # 내가 움직인 뒤의 결과
        
        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == 1:
                location[player] = (nx, ny)
                board[x][y] = 0
                
                match_result.append(game(move+1))
                
                location[player] = (x, y)
                board[x][y] = 1
        
        # 현재 플레이어가 이동할 위치가 없는 경우
        if len(match_result) == 0: 
            return True, move
        
        else:
            # 상대로부터 받은 결과에 True(상대의 패배)가 포합되어 있을 경우
            is_player_win = any(res[0] for res in match_result)
            
            if move == 0:
                # 첫 움직임에서
                if is_player_win:
                    #  플레이어 A가 이길 수 있는 경우
                    answer = min(res[1] for res in match_result if res[0])
                else:
                    answer = max(res[1] for res in match_result)
            
            # 현재 플레이어의 가능한 움직임 중에 상대를 이길 수 있는 경로가 있을 경우
            if is_player_win:
                # 현재 플레이어가 실수를 하지 않는다면 이길 수 있으므로 False, 
                # 이길 경우 최소한의 움직임으로 이겨야 하기 때문에 이길 결과의 움직임 중 min 값을 반환
                return False, min(res[1] for res in match_result if res[0])
            
            else:   
                # 현재 플레이어가 이길 경로가 없으므로 True,
                # 질 경우 최대한 많이 움직여야 하기 때문에 결과 움직임 중 max 값을 반환
                return True, max(res[1] for res in match_result)
    
    game(0)

    return answer