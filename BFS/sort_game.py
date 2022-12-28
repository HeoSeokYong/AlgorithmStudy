# 백준 #1327 소트 게임
'''
    Algorithm: bfs
    Time Complexity: O(N!) ?

    try 1) bfs활용, 모든 경우 해보기
    2 <= N, K <= 8
    범위가 작아서 다행이다.
'''
import sys
from typing import List
from collections import deque

input = sys.stdin.readline

def solution(N: int, K: int, perm: List[str]) -> int:
    ascend_perm = "".join(sorted(perm))
    q = deque([(0, "".join(perm))])
    visited = set(q[0][1])

    def get_rev(l: str, a: int, b: int) -> str:
        ''' l의 a, b 구간을 뒤집은 문자열 반환'''
        res = []
        for i in range(N):
            if a <= i < b:
                res.append(l[a+b-i-1])
            else:
                res.append(l[i])

        return "".join(res)

    while q:
        cnt, p = q.popleft()

        if p == ascend_perm:
            return cnt
        
        for i in range(N-K+1):
            np = get_rev(p, i, i+K)
            if np not in visited:
                q.append((cnt + 1, np))
                visited.add(np)

    return -1


if __name__ == "__main__":
    N, K = map(int, input().split())
    perm = input().split()

    print(solution(N, K, perm))