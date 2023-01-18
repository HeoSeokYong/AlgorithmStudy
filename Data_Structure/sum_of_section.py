# 백준 #2042 구간 합 구하기
'''
    Algorithm: Segment Tree
    Time Complexity: O((M+K)logN)

'''
import sys
import math
from typing import List, Tuple, Callable

sys.setrecursionlimit(10**7)

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, M, K = map(int, input().split())
    nums = [int(input()) for _ in range(N)]
    orders = [tuple(map(int, input().split())) for _ in range(M+K)]
    return N, M, K, nums, orders

class SegmentTree:
    def __init__(self, n: int, nums: List[int]):
        self.tree = [0 for _ in range(4 * self.get_num_node(n))]
        self.nums = nums
        self.build(1, 0, n-1)

    def get_num_node(self, n: int):
        return int(math.pow(2, math.ceil(math.log(n, 2)) + 1) - 1)

    def build(self, node: int, l: int, r: int) -> int:
        if l == r:
            # leaf node
            self.tree[node] = self.nums[l]
        else:
            mid = (l + r) >> 1

            left = self.build(2*node, l, mid)
            right = self.build(2*node+1, mid+1, r)
            self.tree[node] = left + right # 구간 합
        
        return self.tree[node]

    def update(self, node: int, l: int, r: int, idx: int, diff: int) -> None:
        if idx < l or idx > r:
            # 범위 밖
            return

        self.tree[node] += diff
        mid = (l + r) >> 1

        if l != r:
            self.update(node*2, l, mid, idx, diff)
            self.update(node*2+1, mid+1, r, idx, diff)
    
    def query(self, l: int, r: int, a: int, b: int, node: int) -> int:
        ''' a~b 범위의 합을 반환하는 함수 '''
        if a > r or b < l:
            # 구간을 벗어나는 경우
            return 0
        elif a <= l and r <= b:
            # a~b가 구간 안에 있는 경우
            return self.tree[node]
        else:
            mid = (l + r) >> 1
            left = self.query(l, mid, a, b, 2*node)
            right = self.query(mid+1, r, a, b, 2*node+1)
            return left + right


def solution(N: int, M: int, K: int, nums: List[int], orders: List[Tuple]) -> List[int]:
    result = []
    seg_tree = SegmentTree(N, nums)

    for a, b, c in orders:
        if a == 1:
            seg_tree.update(1, 0, N-1, b-1, c - nums[b-1])
            nums[b-1] = c
        elif a == 2:
            result.append(seg_tree.query(0, N-1, b-1, c-1, 1))

    return result


if __name__ == "__main__":
    print(*solution(*read_data()), sep='\n')

