# 백준 #2224 명제 증명
'''
    Algorithm: 플로이드-워셜
    Time Complexity: O(MAXV ^ 3) (MAXV = 52)
    
    try 1) 단순 구현 -> 실패

    try 2) 플로이드-워셜
        boolean 배열로 갈 수 있는 곳을 기록한다.
        i -> k, k -> j 가 가능한 경우,
        i -> j 를 추가로 기록한다. 

        개수를 카운팅하는데 주의할 필요가 있다.
'''
import sys
from typing import List

input = sys.stdin.readline
MAXV = 52
ARROW = ' => '

def ctoi(c: str) -> int:
    if c.isupper():
        return ord(c) - ord('A')
    else:
        return ord(c) - ord('a') + 26

def itoc(i:int) -> str:
    if i < 26:
        return chr(i + ord('A'))
    else:
        return chr(i + ord('a') - 26)

def solution(N: int) -> List[str]:
    floyd = [[False for _ in range(MAXV)] for _ in range(MAXV)]
    cnt = 0

    def get_proposition(a: int, b: int) -> str:
        ''' a, b를 각 수에 해당하는 문자로 바꾸고 a => b로 반환'''
        return itoc(a) + ARROW + itoc(b)

    for _ in range(N):
        a, b = map(ctoi, input().rstrip().split(ARROW))
        if a != b and not floyd[a][b]:
            floyd[a][b] = True
            cnt += 1

    for k in range(MAXV):
        for i in range(MAXV):
            for j in range(MAXV):
                if i != j and not floyd[i][j] and floyd[i][k] and floyd[k][j]:
                    floyd[i][j] = True
                    cnt += 1

    print(cnt)
    return [get_proposition(i, j) for i in range(MAXV) for j in range(MAXV) if floyd[i][j] and i != j]


if __name__ == "__main__":
    N = int(input())

    print(*solution(N), sep='\n')