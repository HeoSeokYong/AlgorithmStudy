# 백준 #1987 알파벳
'''
    Algorithm: set를 활용한 bfs
    Time Complexity: O(N^2) (N = R*C)
'''
import sys

input = sys.stdin.readline

def solution(R, C):
    answer = 0
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

    board = [list(input().rstrip()) for _ in range(R)]
    q = set([(0, 0, board[0][0])])

    while q:
        x, y, alphabet = q.pop()

        answer = max(answer, len(alphabet))

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in alphabet:
                q.add((nx, ny, alphabet + board[nx][ny]))

    return answer


if __name__ == "__main__":
    R, C = map(int, input().split())

    print(solution(R, C))

# ------------------------------------------------------------------#
'''
    Algorithm: dfs, 백트래킹
    Time Complexity: O(N^2) (N = R*C)

    알파벳을 아스키코드로 바꿔 길이 26의 배열로 방문을 관리한다.
'''
'''
import sys

input = sys.stdin.readline

def solution(R, C):
    answer = 0
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

    board = [list(map(lambda x:ord(x)-65, input().rstrip())) for _ in range(R)]
    alphabet = [False] * 26

    def dfs(x, y, d):
        nonlocal answer

        answer = max(answer, d)
        alphabet[board[x][y]] = True

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and not alphabet[board[nx][ny]]:
                dfs(nx, ny, d+1)

        alphabet[board[x][y]] = False

    dfs(0, 0, 1)
    
    return answer


if __name__ == "__main__":
    R, C = map(int, input().split())

    print(solution(R, C))
'''