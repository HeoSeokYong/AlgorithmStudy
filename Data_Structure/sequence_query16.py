# 백준 #14428 수열과 쿼리 16
'''
    Algorithm: segment tree
    Time Complexity: O(MlogN)

'''
import sys
import math
from typing import List, Tuple, Callable

INF = float('inf')

class SegmentTree:
    def __init__(self, n:int, nums:List[int]):
        self.n = n
        self.tree = [(INF, INF) for _ in range(self.get_num_node(n))]
        self.nums = nums
        self.dummy = (INF, INF)
        self.build(1, 0, n-1)

    def get_num_node(self, n:int):
        return int(math.pow(2, math.ceil(math.log(n, 2)) + 1) - 1)

    def build(self, node:int, l:int, r:int) -> int:
        if l == r:
            # leaf node
            self.tree[node] = (self.nums[l], l)
        else:
            mid = (l + r) >> 1

            left = self.build(2*node, l, mid)
            right = self.build(2*node+1, mid+1, r)
            self.tree[node] = min(left, right) # minSegTree

        return self.tree[node]

    def update(self, node:int, idx:int, value:int, l:int, r:int):
        # bottom-up
        while l < r:
            mid = (l + r) >> 1

            if idx > mid:
                l = mid + 1
                node = 2 * node + 1
            else:
                r = mid
                node = 2 * node

        self.nums[idx] = value
        self.tree[node] = (value, idx)

        while node:
            parent_node = node // 2
            self.tree[parent_node] = min(self.tree[parent_node*2], self.tree[parent_node*2 + 1])
            node //= 2
    
    def find(self, node:int, s: int, e:int, l:int, r:int) -> int:
        if s > r or e < l:
            return self.dummy
        
        if s <= l and r <= e:
            return self.tree[node]

        mid = (l + r) >> 1
        left = self.find(2*node, s, e, l, mid)
        right = self.find(2*node+1, s, e, mid+1, r)

        return min(left, right)

    def query(self, ver:int, o1:int, o2:int):
        if ver == 1:
            # Change A[o1] to o2.
            self.update(1, o1-1, o2, 0, self.n-1)

        elif ver == 2:
            # return min of A[o1:o2+1]
            return self.find(1, o1-1, o2-1, 0, self.n-1)[1] + 1


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    return N, A, M


def solution(N:int, A:List[int], M:int) -> List[int]:
    result = []
    seg_tree = SegmentTree(N, A)

    for _ in range(M):
        if res := seg_tree.query(*map(int, input().split())):
            result.append(res)

    return result

if __name__ == "__main__":
    print(*solution(*read_data()), sep='\n')