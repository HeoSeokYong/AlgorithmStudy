import sys
input = sys.stdin.readline

day = 0
M, N, H = map(int, input().split())

box = [[[int(x) for x in input().split()] for _ in range(N)] for __ in range(H)]

q = []
target = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                q.append((i,j,k))
            elif box[i][j][k] == 0:
                target += 1
while True:
    nextq = []
    while q:
        i, j, k = q.pop()
        for di, dj, dk in (
            (1,0,0), (-1,0,0),
            (0,1,0), (0,-1,0),
            (0,0,1), (0,0,-1)):
                ni, nj, nk = i+di, j+dj, k+dk
                if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M:
                    if box[ni][nj][nk] == 0:
                        box[ni][nj][nk] = 1
                        target -= 1
                        nextq.append((ni,nj,nk))
    if nextq:
        day += 1
    else:
        break
    q = nextq

answer = day if target==0 else -1
print(answer)