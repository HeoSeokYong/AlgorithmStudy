from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

def dummy(apple_box, change_dir):
    x, y, t = 0, 0, 0
    sneak = deque([(x, y)])
    dir = 0 # R로 시작
    
    while True:
        t += 1
        # move head
        if dir == 0: # R
            y += 1
        elif dir == 1: # D
            x += 1
        elif dir == 2: # L
            y -= 1
        elif dir == 3: # U
            x -= 1

        # break check
        if (x, y) in sneak:
            break
        if x < 0 or x >= n or y < 0 or y >= n:
            break

        sneak.append((x,y))

        # apple check
        if (x, y) not in apple_box:
            sneak.popleft()
        else:
            apple_box.remove((x,y))

        # change dir check
        if t in change_dir.keys():
            if change_dir[t] == 'L':
                dir = (dir-1) % 4
            elif change_dir[t] == 'D':
                dir = (dir+1) % 4
    
    return t

# apple info
k = int(input())
apple_box = []
for i in range(k):
    r, c = map(int, input().split())
    apple_box.append((r-1, c-1))

# dir info
l = int(input())
change_dir = {}
for i in range(l):
    x, c = input().split()
    change_dir[int(x)] = c

print(dummy(apple_box, change_dir))