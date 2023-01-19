# 백준 # 구간 곱 구하기
'''
    Algorithm: Segment Tree
    Time Complexity: O((M+K)logN)

    update를 할 때 위에서부터 내려오면 0의 처리가 힘들었다.
    => 해당하는 leaf node를 찾고 거기서 루트 노드까지 올라오면서 갱신하는 방식
'''
import sys
import math
from typing import List, Tuple, Callable

LIMIT = 1000000007

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N, M, K = map(int, input().split())
    nums = [int(input()) for _ in range(N)]
    order = [tuple(map(int, input().split())) for _ in range(M+K)]
    return N, M, K, nums, order


class SegmentTree:
    def __init__(self, n: int, nums: List[int]):
        self.tree = [0 for _ in range(self.get_node_cnt(n))]
        self.nums = nums
        self.build(1, 0, n-1)
    
    def get_node_cnt(self, n: int) -> int:
        return int(math.pow(2, math.ceil(math.log(n, 2)) + 1) - 1)

    def build(self, node: int, l: int, r: int) -> int:
        if l == r:
            # leaf node
            self.tree[node] = self.nums[l]
        else:
            mid = (l + r) >> 1

            left = self.build(2*node, l, mid)
            right = self.build(2*node+1, mid+1, r)
            self.tree[node] = (left * right) % LIMIT

        return self.tree[node]

    def update(self, node: int, l: int, r: int, idx: int, target: int):
        ''' 재귀가 아닌 반복문을 사용해 바텀업 방식으로 구현 '''
        # idx의 노드 위치 찾기
        while l < r:
            mid = (l + r) >> 1

            if idx > mid:
                l = mid + 1
                node = node * 2 + 1
            else:
                r = mid
                node = node*2
        
        self.tree[node] = target
        
        while node:
            parent_node = node // 2
            self.tree[parent_node] = (self.tree[parent_node*2] * self.tree[parent_node*2+1]) % LIMIT
            node //= 2

    def query(self, node: int, l: int, r: int, a: int, b: int) -> int:
        if r < a or  l > b:
            # 구간 밖
            return 1
        elif a <= l and r <= b:
            # l~r 가 구간 a~b 안에 있는 경우
            return self.tree[node]
        else:
            mid = (l + r) >> 1

            left = self.query(2*node, l, mid, a, b)
            right = self.query(2*node+1, mid+1, r, a, b)
            return int((left * right) % LIMIT)


def solution(N: int, M: int, K: int, nums: List[int], order: List[Tuple]) -> List[int]:
    result = []
    seg_tree = SegmentTree(N, nums)

    for a, b, c in order:
        if a == 1:
            seg_tree.update(1, 0, N-1, b-1, c)
        elif a == 2:
            result.append(seg_tree.query(1, 0, N-1, b-1, c-1))

    return result


if __name__ == "__main__":
    print(*solution(*read_data()), sep='\n')

