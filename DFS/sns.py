# 백준 #2533 사회망 서비스(SNS)
'''
    Algorithm: dp, dfs
    Time Complexity: O(N)
    
    dp[i][0]: i번째 노드가 얼리 어답터일 경우 자식들의 얼리어답터 수
    dp[i][1]: i번째 노드가 얼리 어답터가 아닐 경우 자식들의 얼리어답터 수 
'''
import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def solution(N):
    dp = [[1, 0] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    tree = [[] for _ in range(N+1)]
    
    def dfs(u):
        visited[u] = True

        for v in tree[u]:
            if not visited[v]:
                dfs(v)
                dp[u][0] += min(dp[v])
                dp[u][1] += dp[v][0]
                

    for _ in range(N-1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    dfs(1)
    print(min(dp[1]))


if __name__ == "__main__":
    N = int(input())

    solution(N)