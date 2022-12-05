# 백준 #1079 마피아
'''
    Algorithm: brute-force, backtracking
    Time Complexity: -

    try 1) 은진의 유죄 지수를 가장 낮게 올리는 방식의 greedy:
        - 틀렸다.
    
    try 2) 수의 범위가 크지 않으니 brute-force with dfs.
        백트래킹을 하지 않으면 시간초과가 난다.
            - 최대 시간복잡도가 거의 15!을 넘어가는듯 ?

        -> 마지막까지 살아남는 경우를 flag로 그 이후 dfs 탐색을 종료시켰다.
'''
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
INF = 1e7

def solution(N, R, guilty, eunjin):
    day = 0
    flag = False
    
    def dfs(survivor, t):
        nonlocal day, flag

        if flag:
            return
        
        if survivor % 2: # afternoon
            target, maxval = 0, 0
            for i in range(N):
                if guilty[i] > maxval:
                    maxval = guilty[i]
                    target = i

            val = guilty[target]

            if target == eunjin:
                day = max(day, t)
                return

            guilty[target] = -INF
            dfs(survivor - 1, t)
            guilty[target] = val

        else: # night
            if survivor == 2:
                day = max(day, t+1)
                flag = True
                return

            for i in range(N):
                if i != eunjin and guilty[i] != -INF:
                    val = guilty[i]
                    guilty[i] = -INF
                    for j in range(N):
                        if guilty[j] != -INF:
                            guilty[j] += R[i][j]

                    dfs(survivor - 1, t+1)
                    for j in range(N):
                        if guilty[j] != -INF:
                            guilty[j] -= R[i][j]
                    guilty[i] = val

    dfs(N, 0)

    return day


if __name__ == "__main__":
    N = int(input())
    guilty = list(map(int, input().split()))
    R = [list(map(int, input().split())) for _ in range(N)]
    eunjin = int(input())

    print(solution(N, R, guilty, eunjin))