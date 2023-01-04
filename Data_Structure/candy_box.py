# 백준 #2243 사탕상자
'''
    Algorithm: segment tree, binary search
    Time Complexity: O(NlogM) (M: 사탕의 맛 범위)

    segment tree로 log 시간복잡도
    사탕의 맛으로 트리를 구성
'''
import sys
from typing import List, Tuple

input = sys.stdin.readline
MAX_TASTE = 1000000

class SegmentTree:
    def __init__(self, X):
        self.tree = [0 for _ in range(4 * X)] # tree의 크기는 넉넉하게 4배

    def update(self, node: int, s: int, e: int, idx: int, diff: int) -> None:
        if idx < s or idx > e:
            return
        
        self.tree[node] += diff
        mid = (s + e) >> 1
        
        if s != e:
            self.update(node*2, s, mid, idx, diff)
            self.update(node*2+1, mid+1, e, idx, diff)
    
    def query(self, node: int, s: int, e: int, n: int) -> int:
        ''' n 번째 순서의 맛 번호 반환 '''
        if s == e:
            return s
        
        mid = (s + e) >> 1

        if n <= self.tree[node*2]: # 왼쪽 자식 노드
            return self.query(2*node, s, mid, n)
        else:
            return self.query(2*node+1, mid+1, e, n - self.tree[node*2])


def solution(N: int, orders: List[Tuple[int]]) -> None:
    candy_box = SegmentTree(MAX_TASTE)

    for order in orders:
        if order[0] == 1:
            candy = candy_box.query(1, 0, MAX_TASTE, order[1])
            candy_box.update(1, 0, MAX_TASTE, candy, -1)
            print(candy)

        else: # order[0] == 2
            candy_box.update(1, 0, MAX_TASTE, order[1], order[2])


if __name__ == "__main__":
    N = int(input())
    orders = [tuple(map(int, input().split())) for _ in range(N)]

    solution(N, orders)