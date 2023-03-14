# 백준 #16235 나무 재테크
'''
    Algorithm: 구현
    Time Complexity: O(KN^2)

    입력으로 주어지는 나무의 위치는 모두 서로 다름.
    PyPy3 통과(1056 ms), Python3 시간초과
    => 시간복잡도를 줄여보자.
    
    1. 리스트를 sorted해서 사용 -> deque으로 대체
        PyPy3 기준 1056 ms -> 976 ms

    2. 4계절 별로 나눠서 진행(봄, 여름, 가을, 겨울) (976 ms -> 784 ms)
    -> 같이할 수 있는 것은 같이 하게 함(봄여름겨울, 가을)

    3. 이것저것 (784 ms -> 700 ms)
        - 리스트 크기 N+1 -> N
        - num_tree를 통해 매번 카운트 -> 마지막에 한번에

    4. 글로벌에서 실행 (700 ms -> 656ms)
    5. 모듈화 (PyPy3 656 ms -> 576 ms, Python3 42%)

'''
import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())

A = tuple(tuple(map(int, input().split())) for _ in range(N))

def adj():
    # generator 생성
    yield 0, 1
    yield 1, 0
    yield -1, 0
    yield 0, -1
    yield 1, 1
    yield 1, -1
    yield -1, 1
    yield -1, -1

farm = [[5 for _ in range(N)] for _ in range(N)] # 농장의 양분
farm_tree = [[deque() for _ in range(N)] for _ in range(N)] # 농장의 나무

for _ in range(M):
    x, y, age = map(int,input().split())
    farm_tree[x-1][y-1].append(age)

def SSW():
    for x in range(N):
        for y in range(N):
            if farm_tree[x][y]:
                grown_tree = deque()
                dead_tree_nutrient = 0

                for tree_age in farm_tree[x][y]:
                    if farm[x][y] >= tree_age:
                        farm[x][y] -= tree_age
                        grown_tree.append(tree_age + 1)
                        if (tree_age + 1) % 5 == 0:
                            propagate_trees.append((x, y))
                    else:
                        dead_tree_nutrient += (tree_age // 2)
        
                # spring
                farm_tree[x][y] = grown_tree
                # summer
                farm[x][y] += dead_tree_nutrient
            # winter
            farm[x][y] += A[x][y]

def F():
    # fall
    for x, y in propagate_trees:
        for dx, dy in adj():
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                farm_tree[nx][ny].appendleft(1)


for year in range(K):
    propagate_trees = []
    SSW()
    F()

print(sum(sum(map(len, farm_tree[x])) for x in range(N)))

