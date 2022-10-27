# 프로그래머스 2021 카카오 채용연계형 인턴십 #2 거리두기 확인하기
'''
    Algorithm: bfs?
    Time Complexity: -
'''
def solution(places):
    ROW, COL, ROOM = 5, 5, 5
    PERSON, EMPTY, PARTITION = 'P', 'O', 'X'

    result = []
    dxdy = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def check_everywhere(k, i, j):
        ''' 주변에 사람이 있는지 확인, 있다: False, 없다: True'''
        for di, dj in dxdy:
            ni, nj = i + di, j + dj

            if 0 <= ni < COL and 0 <= nj < ROW:
                if places[k][ni][nj] == PERSON:
                    return False
                elif places[k][ni][nj] == EMPTY:
                    for dx, dy in dxdy:
                        nx, ny = ni + dx, nj + dy

                        if 0 <= nx < COL and 0 <= ny < ROW:
                            if (nx, ny) != (i, j) and places[k][nx][ny] == PERSON:
                                return False
        return True
                
    for k in range(ROOM):
        flag = True

        i = 0
        while flag and i < COL:
            j = 0
            while flag and j < ROW:
                if places[k][i][j] == PERSON:
                    flag = check_everywhere(k, i, j)
                j += 1
            i += 1

        result.append(1 if flag else 0)

    return result

if __name__ == "__main__":
    places = [["OPOOP", "PXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

    print(solution(places))

''' 예전에 풀었던 코드 -----------------------------------------------

def solution(places):
    answer = []
    ls = [(1,1), (1,-1)]
    ls2 = [(2,0), (0,2)]
    
    for pla in places:
        flag = False
        # Room check
        for i in range(len(pla)): 
            for j in range(len(pla[0])):
                if pla[i][j] == 'P':
                    # 오른쪽, 아래
                    if (i < 4 and pla[i+1][j] == 'P') or (j < 4 and pla[i][j+1] == 'P'):
                            flag=True
                            break
                    # 대각선(우하, 좌하)
                    for a, b in ls:
                        if i<4 and (0 <= j+b < 5):
                            if pla[i+a][j+b] == 'P':
                                if pla[i+1][j] != 'X' or pla[i][j+b] != 'X':
                                    flag=True
                                    break
                    # 2칸 오른쪽, 아래
                    for a,b in ls2:
                        if i+a < 5 and j+b < 5:
                            if pla[i+a][j+b] == 'P':
                                if pla[i+(a//2)][j+(b//2)] != 'X':
                                    flag = True
                                    break

            if flag:
                break
        if flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer
'''