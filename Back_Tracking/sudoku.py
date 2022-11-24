# 백준 #2239 스도쿠
'''
    Algorithm: dfs, backtracking
    Time Complexity: -
    pypy3 통과
    python3 시간초과
'''
import sys

input = sys.stdin.readline

def solution(sudoku: list[list[int]]) -> list[list[int]]:
    blanks = []
    note = {'row': [set() for _ in range(9)], \
            'col': [set() for _ in range(9)], \
            'sec': [set() for _ in range(9)]}

    def xy2sec(x, y):
        return 3 * (x // 3) + (y // 3)

    def dfs(idx):
        if idx == len(blanks):
            # 마지막 빈칸까지 채워서 넘어온 경우 True
            return True

        x, y = blanks[idx]
        sec_idx = xy2sec(x,y)

        for i in range(1, 10):
            if i not in note['row'][x] and \
               i not in note['col'][y] and \
               i not in note['sec'][sec_idx]:
                note['row'][x].add(i)
                note['col'][y].add(i)
                note['sec'][sec_idx].add(i)
                sudoku[x][y] = i

                # 다음 빈칸을 검사
                if dfs(idx+1): 
                    return True

                note['row'][x].remove(i)
                note['col'][y].remove(i)
                note['sec'][sec_idx].remove(i)
                sudoku[x][y] = 0

        return False

    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                blanks.append((i, j))
            else:
                num = sudoku[i][j]
                note['row'][i].add(num)
                note['col'][j].add(num)
                note['sec'][xy2sec(i, j)].add(num)

    dfs(0)

    return sudoku


if __name__ == "__main__":
    sudoku = [[int(x) for x in input().rstrip()] for _ in range(9)]
    sudoku = solution(sudoku)

    for i in range(9):
        print(*sudoku[i], sep='')