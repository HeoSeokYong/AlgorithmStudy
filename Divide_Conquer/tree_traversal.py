import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())

in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

position = [0] * (n+1)
for i in range(n):
    position[in_order[i]] = i

def preorder(inStart, inEnd, postStart, postEnd):
    if inStart > inEnd or postStart > postEnd:
        return
    
    root = post_order[postEnd]
    print(root, end=' ')

    left = position[root] - inStart
    right = inEnd - position[root]

    preorder(inStart, position[root] - 1, postStart, postStart + left - 1)
    preorder(position[root] + 1, inEnd, postEnd - right, postEnd - 1)

preorder(0, n-1, 0, n-1)

