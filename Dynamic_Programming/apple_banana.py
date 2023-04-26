# 백준 #3114 사과와 바나나
'''
    Algorithm: dp, 누적합
    Time Complexity: O(RC)

    위에서 아래로 누적합을 이용

    dp[i][j] = 왼쪽(i, j-1), 위(i-1, j), 왼쪽위(i-1, j-1)에서 온 경우 중 최댓값
        - 왼쪽에서 온 경우, 왼위에서 온 경우
            현 위치의 사과+바나나를 더해준다.
        - 위에서 온 경우
            현 위치의 사과나무 개수를 빼준다.

'''
import sys
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    R, C = map(int, input().split())
    apple_tree = [[0 for _ in range(C+1)] for _ in range(R+1)]
    banana_tree = [[0 for _ in range(C+1)] for _ in range(R+1)]
    
    for i in range(1, R+1):
        inps = input().split()
        
        for j in range(1, C+1):
            inp = inps[j-1]
            fruit, num = inp[0], int(inp[1:])

            if fruit == 'A':
                apple_tree[i][j] = num
            else:
                banana_tree[i][j] = num

    return R, C, apple_tree, banana_tree


def solution(R:int, C:int, apple_tree:List[List[str]], banana_tree:List[List[str]]) -> int:
    dp = [[0 for _ in range(C+1)] for _ in range(R+1)]

    # 밑으로 누적합
    for i in range(1, R+1):
        for j in range(1, C+1):
            apple_tree[i][j] += apple_tree[i-1][j]
            banana_tree[i][j] += banana_tree[i-1][j]

    for i in range(1, R+1):
        for j in range(1, C+1):
            if j == 1:            
                # B가 0개를 가지는 경우
                dp[i][j] = apple_tree[R][j] - apple_tree[i][j]
            else:
                ab_sum = apple_tree[R][j] - apple_tree[i][j] + banana_tree[i-1][j] # (i, j) 에서의 사과+바나나
                dp[i][j] = max(dp[i-1][j] - (apple_tree[i][j] - apple_tree[i-1][j]), dp[i][j-1] + ab_sum, dp[i-1][j-1] + ab_sum)

    return dp[R][C]


if __name__ == "__main__":
    print(solution(*read_data()))
