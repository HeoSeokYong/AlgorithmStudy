import sys
input = sys.stdin.readline

answer = [0]
n, m = map(int, input().split())
relation = {i:[] for i in range(n)}

for i in range(m):
    a, b = map(int, input().rstrip('\n').split())
    relation[a].append(b)
    relation[b].append(a)

def dfs(visited, lev, cur):
    if lev == 4:
        answer[0] = 1
        return
    for r in relation[cur]:
        if not visited[r]:
            visited[r] = True
            dfs(visited, lev+1, r)
            visited[r] = False

        
for i in range(n):
    visited = [False] * n
    visited[i] = True
    dfs(visited, 0, i)

print(answer[0])