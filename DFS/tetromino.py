# 백준 #14500 테트로미노
'''
    Algorithm: dfs
    Time Complexity: -

'''
import sys

input = sys.stdin.readline

def solution(N, M):
    answer = 0
    paper = [list(map(int, input().split())) for _ in range(N)]
    MAX_NUM = max(max(p) for p in paper)
    dxdy = ((0, 1), (1, 0), (0, -1), (-1, 0))
    visited = [[False for _ in range(M)] for _ in range(N)]

    def dfs(x, y, res, cnt):
        nonlocal answer

        # 최대의 경우로 진행해도 answer을 갱신 못하는 경우
        if res + MAX_NUM * (4-cnt) <= answer:
            return

        if cnt == 4:
            answer = max(answer, res)
            return 

        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if cnt == 2: # ㅗ 자 블럭을 위한 분기
                    visited[nx][ny] = True
                    dfs(x, y, res+paper[nx][ny], cnt+1)
                    visited[nx][ny] = False

                visited[nx][ny] = True
                dfs(nx, ny, res+paper[nx][ny], cnt+1)
                visited[nx][ny] = False


    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(i, j, paper[i][j], 1)
            visited[i][j] = False

    return answer


if __name__ == "__main__":
    N, M = map(int, input().split())

    print(solution(N, M))