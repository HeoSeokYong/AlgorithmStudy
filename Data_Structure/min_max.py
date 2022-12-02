# 백준 #2357 최솟값과 최댓값
'''
    Algorithm: Segment Tree
    Time Complexity: O(MlogN)
    
    Segment Tree 자료구조를 활용해 리스트에서의 연산의 시간을 줄인다.
'''
import sys

input = sys.stdin.readline
INF = 10**9
sys.setrecursionlimit(INF)

class SegmentTree:
    def __init__(self, nums: list[int], func: str('max' or 'min')) -> None:
        self.dummy = 0 if func == 'max' else INF
        self.tree = [self.dummy for _ in range(4 * len(nums))] # tree의 크기는 넉넉하게 4배
        self.nums = nums
        self.func = eval(func)
        self.build(1, 0, len(nums)-1)

    def build(self, node: int, l: int, r: int) -> int:
        if l == r: # leaf node
            self.tree[node] = self.nums[l]
            return self.tree[node]

        mid = (l + r) // 2
        left = self.build(2*node, l, mid)
        right = self.build(2*node+1, mid+1, r)
        self.tree[node] = self.func(left, right)

        return self.tree[node]
        
    def find(self, start: int, end: int, node: int, l: int, r: int) -> int:
        # 범위를 벗어나는 경우
        if start > r or end < l:
            return self.dummy

        # l ~ r이 start ~ end 범위 안에 있는 경우
        if start <= l and r <= end:
            return self.tree[node]
        
        mid = (l + r) // 2
        left = self.find(start, end, 2*node, l, mid)
        right = self.find(start, end, 2*node+1, mid+1, r)
        
        return self.func(left, right)

def solution(N: int, M: int) -> list[list[int]]:
    result = []
    nums = [int(input()) for _ in range(N)]
    maxSeg = SegmentTree(nums, 'max')
    minSeg = SegmentTree(nums, 'min')

    for _ in range(M):
        s, e = map(int, input().split())

        result.append([minSeg.find(s-1, e-1, 1, 0, len(nums)-1), maxSeg.find(s-1, e-1, 1, 0, len(nums)-1)])

    return result


if __name__ == "__main__":
    N, M = map(int, input().split())

    for sol in solution(N, M):
        print(*sol)