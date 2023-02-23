# 백준 #5639 이진 검색 트리
'''
    Algorithm: 트리, 재귀
    Time Complexity: O(N^2)

    try 1) 객체로 구현하니까 무거워서 시간 초과(Python3), 메모리 초과(PyPy3)

    try 2) 그냥 배열로 구현하자.
    배열에서 루트 노드보다 큰 수가 나오면 거기서부터 오른쪽 노드이다.
'''
import sys
from typing import Callable

sys.setrecursionlimit(10**8)

# class Node:
#     def __init__(self, data:int):
#         self.value = data
#         self.left = None
#         self.right = None

# class BinarySearchTree:
#     def __init__(self, root:int):
#         self.head = Node(root)

#     def add_node(self, node:Node, data:int):
#         if data > node.value:
#             if node.right:
#                 self.add_node(node.right, data)
#             else:
#                 node.right = Node(data)
#         else:
#             if node.left:
#                 self.add_node(node.left, data)
#             else:
#                 node.left = Node(data)
    
#     def postorder_traversal(self, node:Node):
#         if node.left:
#             self.postorder_traversal(node.left)
#         if node.right:
#             self.postorder_traversal(node.right)
#         print(node.value)
        

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def solution() -> int:
    tree = []

    def postorder_traversal(l:int, r:int):
        if l >= r:
            return

        mid = r
        
        # 현재 범위에서 l(현재 범위의 루트 노드) 보다 큰 값을 찾는다.
        for i in range(l+1, r):
            if tree[l] < tree[i]:
                mid = i
                break

        # 왼쪽 서브트리
        postorder_traversal(l+1, mid) 
        # 오른쪽 서브트리
        postorder_traversal(mid, r)

        print(tree[l])

    # main
    while True:
        try:
            x = int(input())
            tree.append(x)
        except:
            break
        
    postorder_traversal(0, len(tree))


if __name__ == "__main__":
    solution()
