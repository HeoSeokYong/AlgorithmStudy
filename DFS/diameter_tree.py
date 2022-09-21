import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

### 1 ###
# n = int(input())
# maxd = 0

# tree = dict()
# for i in range(n):
#     tree[i+1] = []
# for i in range(n-1):
#     a, b, c = map(int, input().split())
#     tree[a].append((b, c))

# def dfs(n, w):
#     l, r = 0, 0
#     for node, weight in tree[n]:
#         d = dfs(node, weight)
#         if l <= r:
#             l = max(l, d)
#         else:
#             r = max(r, d)
#     global maxd
#     maxd = max(maxd, l+r)
#     return max(l+w, r+w)

# dfs(1, 0)
# print(maxd)

### 2 ###
v = int(input())
maxd = 0
lastn = 0
tree = dict()
for i in range(v):
    tree[i+1] = []

for _ in range(v):
    info = list(map(int, input().split()))[:-1]
    for i in range(len(info)//2):
        tree[info[0]].append((info[2*i+1], info[2*i+2]))

def dfs(n, w, visited):
    dist = []
    visited[n] = 1
    for node, weight in tree[n]:
        if visited[node] == 0:
            global lastn
            lastn = node
            dist.append(dfs(node, weight, visited))
    global maxd
    if len(dist) > 1:
        dist.sort(reverse=True)
        l, r = dist[:2]
        maxd = max(maxd, l+r)
        return max(l+w, r+w)
    elif len(dist) == 1:
        maxd = max(dist[0], maxd)
        return dist[0] + w
    else:
        return w

visit = [0] * (v+1)
dfs(1, 0, visit)
visit = [0] * (v+1)
dfs(lastn, 0, visit)

print(maxd)