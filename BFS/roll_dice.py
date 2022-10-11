# 백준 #23288 주사위 굴리기 2
'''
    알고리즘: 구현, bfs
'''
import sys
from collections import deque

input = sys.stdin.readline
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 동남서북 시계방향 순서

def get_score(N, M, dice, world):
    score = 0
    r, c = dice['loc']
    B = world[r][c]

    # bfs
    q = deque([(r, c)])
    visited = set()
    visited.add((r, c))
    
    while q:
        x, y = q.popleft()
        score += 1

        for dx, dy in direction:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and world[nx][ny] == B and (nx, ny) not in visited:
                q.append((nx, ny))
                visited.add((nx, ny))
            
    return B * score

def roll_dice(dice):
    if dice['dir'] % 2 == 0: # E or W
        if dice['dir'] == 0: # E
            dice['state']['w'].rotate(1)
        else: # W
            dice['state']['w'].rotate(-1)

        # 주사위의 위와 밑 부분을 같게 해줌
        dice['state']['h'][1] = dice['state']['w'][1]
        dice['state']['h'][3] = dice['state']['w'][3]

    else: # N or S
        if dice['dir'] == 3: # N
            dice['state']['h'].rotate(-1)
        else: # S
            dice['state']['h'].rotate(1)

        dice['state']['w'][1] = dice['state']['h'][1]
        dice['state']['w'][3] = dice['state']['h'][3]

    return dice

def solution(N, M, K, world):
    answer = 0
    dice = {'loc': (0, 0), 'dir': 0}
    # w: 서 위 동 밑 / h: 북 위 남 밑
    dice['state'] = {'w': deque([4, 1, 3, 6]), 'h': deque([2, 1, 5, 6])}

    while K:
        x, y = dice['loc']
        dx, dy = direction[dice['dir']]

        nx, ny = x + dx, y + dy
        
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            dice['dir'] = (dice['dir'] + 2) % 4
            nx, ny = x - dx, y - dy

        dice['loc'] = (nx, ny)
        dice = roll_dice(dice)

        answer += get_score(N, M, dice, world)
        
        if dice['state']['w'][3] > world[nx][ny]:
            dice['dir'] = (dice['dir'] + 1) % 4
        elif dice['state']['w'][3] < world[nx][ny]:
            dice['dir'] = (dice['dir'] - 1) % 4

        K -= 1

    return answer


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    world = [list(map(int, input().split())) for _ in range(N)]

    print(solution(N, M, K, world))