# 백준 #12100 2048 (Easy)
'''
    Algorithm: brute-foce, 백트래킹
    Time Complexity: -

    - brute-force
    백트래킹으로 어느 정도 줄이면 시간 안에 가능할 듯 하다.
'''
import sys
from typing import List, Tuple, Callable

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    return N, board


def solution(N: int, board: List[List[int]]) -> int:
    result = 0
    dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def check_max_block(board: List[List[int]]) -> int:
        return max(map(max, board))

    def move(board: List[List[int]], diridx: int) -> List[List[int]]:
        dx, dy = dxdy[diridx] # diridx == 0: right, 1: down, 2: left, 3: up
        visited = set() # 이번 움직임에서 이미 합쳐진 블록을 기록

        for i in range(N):
            for move in range(N-2, -1, -1) if diridx < 2 else range(1, N):
                x, y = (move, i) if diridx % 2 else (i, move) # 각 움직임 별로 움직이는 변수에 move를 할당

                # 블록에 숫자가 있을 경우 움직일 위치를 찾는다.
                if board[x][y] != 0:
                    mx, my = x + dx, y + dy

                    while 0 <= mx < N and 0 <= my < N and board[mx][my] == 0:
                        mx, my = mx + dx, my + dy

                    # 이동할 블록이 끝 부분(board를 넘어선)일 경우 한 칸 전으로
                    if (diridx < 2 and max(mx, my) == N) or (diridx >= 2 and min(mx, my) == -1):
                        mx, my = mx - dx, my - dy
                    # 이동할 블록의 숫자가 현 숫자와 다르거나 이미 합쳐진 블록일 경우 한 칸 전으로
                    elif board[mx][my] != board[x][y] or (mx, my) in visited:
                        mx, my = mx - dx, my - dy
                    # 이동할 블록의 숫자가 현 숫자와 같을 경우 2배로 처리
                    elif board[mx][my] == board[x][y]:
                        board[x][y] *= 2
                        visited.add((mx, my))
                    # 이동할 위치가 현 위치가 아닐 경우 블록을 움직인다.
                    if (mx, my) != (x, y):
                        board[mx][my] = board[x][y]
                        board[x][y] = 0
        return board

    def game(turn: int, board: List[List[int]]):
        nonlocal result

        if turn == 5:
            result = max(result, check_max_block(board))
            return

        for i in range(4):
            game(turn + 1, move([b[:] for b in board], i))

    # main
    game(0, board)
    return result


if __name__ == "__main__":
    print(solution(*read_data()))

