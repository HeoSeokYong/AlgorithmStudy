# 백준 #16724 피리 부는 사나이
'''
    Algorithm: 그래프 탐색(DFS?), 분리 집합
    시간복잡도: O(2*N*M) = 약 2,000,000
'''
import sys

input = sys.stdin.readline
direction = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}

def solution(N, M, maps):
    '''
        maps의 방문하지 않은 모든 곳을 탐색.
        group_num: 그룹 구분을 위한 변수
        visited: 기본값 0 에서 방문시 group_num 값으로 path별 그룹 분리
        answer: path가 자기 자신으로 돌아온 경우 safe zone +1 추가,
                다른 그룹과 만난 경우 그 그룹의 safe zone 이용.
    '''
    answer, group_num = 0, 0
    visited = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                x, y = i, j
                group_num += 1

                while True:
                    visited[x][y] = group_num
                    
                    dx, dy = direction[maps[x][y]]
                    nx, ny = x + dx, y + dy

                    if not visited[nx][ny]:
                        x, y = nx, ny
                    else:
                        if visited[nx][ny] == group_num:
                            answer += 1
                        break
                
    return answer

if __name__ == "__main__":
    N, M = map(int, input().split())
    maps = [input() for _ in range(N)]

    print(solution(N, M, maps))
