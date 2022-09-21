import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
tree = dict()
for i in range(N):
    tree[i+1] = []
for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
def solution(tree):
    q = deque([1])
    parent = [0] * (N-1)
    while q:
        idx = q.popleft()
        for t in tree[idx]:
            if parent[t-2] == 0 and t != 1:
                parent[t-2] = idx
                q.append(t)
    
    return parent

for s in solution(tree):
    print(s)