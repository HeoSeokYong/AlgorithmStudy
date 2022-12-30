# 백준 #16940 BFS 스페셜 저지
'''
    Algorithm: bfs
    Time Complexity: O(N)

    try 1) 진입차수를 활용한 방법
        -> 같은 차수라도 진입 순서에 따른 차이가 있다.

    try 2) 정답을 그대로 진행하며 확인하기
        set로 구성된 덱을 활용해서 구현
'''
import sys
from typing import List
from collections import deque

input = sys.stdin.readline

def solution(N: int, tree: List[List[int]], answer: List[int]) -> int:
    q = deque([1])
    visited = set([1])
    cand = deque()
    idx = 1

    while q:
        cur_node = q.popleft()
        cand.append(set())

        for next_node in tree[cur_node]:
            
            if next_node not in visited:
                cand[-1].add(next_node)

        if answer[idx] not in cand[0]:
            break

        else:
            q.append(answer[idx])
            cand[0].remove(answer[idx])
            visited.add(answer[idx])
            idx += 1
        
        if idx == N:
            break

        while cand and not cand[0]:
            cand.popleft()

    return int(idx == N)


if __name__ == "__main__":
    N = int(input())
    tree = [[] for _ in range(N+1)]

    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    answer = list(map(int, input().split()))

    print(solution(N, tree, answer))