# 백준 #14503 로봇청소기
'''
    Algorithm: 구현
    Time Complexity: O(NM)

    room => 0: not clean, 1: wall, 2: clean
'''
import sys
from typing import List, Tuple, Callable

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, M = map(int, input().split())
    robot_info = list(map(int, input().split()))
    room = [list(map(int, input().split())) for _ in range(N)]
    return N, M, robot_info, room


def solution(N:int, M:int, robot_info:List[int], room:List[List[int]]) -> int:
    result = 1

    # N E S W
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    x, y, cur_dir = robot_info

    while True:
        room[x][y] = 2

        is_dirty = False
        
        for i in range(1, 5):
            ni = (cur_dir - i) % 4 # counter-clockwise
            nx, ny = x + dx[ni], y + dy[ni]

            if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
                is_dirty = True
                break
    
        if is_dirty: # move and clean
            x, y, cur_dir = nx, ny, ni
            result += 1
        else: # go back
            nx, ny = x - dx[cur_dir], y - dy[cur_dir]

            if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 2:
                x, y, cur_dir = nx, ny, ni
            else: # end
                break

    return result


if __name__ == "__main__":
    print(solution(*read_data()))

