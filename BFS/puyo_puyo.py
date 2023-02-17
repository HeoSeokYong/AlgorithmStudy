# 백준 #11559 Puyo Puyo
'''
    Algorithm: bfs, 구현
    Time Complexity: -

'''
import sys
from typing import List, Tuple, Callable
from collections import deque

ROW, COL = 12, 6

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    field = [list(input()) for _ in range(ROW)]
    return field,


def solution(field:List[List[str]]) -> int:
    combo = 0
    dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def play() -> bool:
        ''' field를 검사하고 뿌요가 터진 경우가 있으면 True 없다면 False 반환 '''
        visited = [[False for _ in range(COL)] for _ in range(ROW)]
        is_crashed = False

        def crash(r:int, c:int) -> bool:
            ''' bfs로 같은 색상의 근처 뿌요를 찾고 4개 이상이면 터트린다. '''
            q = deque([(r, c)])
            color = field[r][c]
            puyo = set()

            while q:
                x, y = q.popleft()

                for dx, dy in dxdy:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < ROW and 0 <= ny < COL and field[nx][ny] == color and (nx, ny) not in puyo:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        puyo.add((nx, ny))
            
            if len(puyo) >= 4:
                for x, y in puyo:
                    field[x][y] = '.'
                return True

            return False
            
        def down():
            ''' 각 뿌요를 바닥으로 떨어지게 한다. '''
            for j in range(COL):
                idx = ROW-1
                for i in range(ROW-1, -1, -1):
                    if field[i][j] != '.':
                        tmp = field[i][j]
                        field[i][j] = '.'
                        field[idx][j] = tmp
                        idx -= 1

        # check field
        for i in range(ROW-1, -1, -1):
            for j in range(COL):
                if field[i][j] != '.' and not visited[i][j]:
                    if crash(i, j):
                        is_crashed = True
        down()

        return is_crashed
    
    # main
    while play(): 
        combo += 1

    return combo


if __name__ == "__main__":
    print(solution(*read_data()))
