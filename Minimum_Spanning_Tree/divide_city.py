# 백준 #1647 도시 분할 계획
'''
    알고리즘: 최소신장트리(크루스칼 알고리즘)
    시간복잡도: O(MlogM + M) -> 약 2천만
    Python 통과 (3912 ms)
'''
import sys

input = sys.stdin.readline

def solution(N, M, path):
    '''
        Kruskal Algorithm
        1. 주어진 모든 간선 정보에 대해 간선 비용이 낮은 순서(오름차순)로 정렬을 수행한다.
        2. 정렬된 간선 정보를 확인하면서 현재의 간선이 노드 간의 사이클을 발생 시키는지 확인
        3. 만약 사이클이 발생하지 않은 경우, 최소 신장 트리에 포함 시키고 사이클이 발생한 경우,
         최소 신장 트리에 포함 시키지 않음
    '''
    answer = 0
    max_cost = 0
    parents = [i for i in range(N+1)]

    def find_parent(x):
        if parents[x] != x:
            parents[x] = find_parent(parents[x])
        return parents[x]
    
    def union_parent(x, y):
        x = find_parent(x)
        y = find_parent(y)
        if x < y:
            parents[y] = x
        else:
            parents[x] = y

    # 1
    path.sort()

    # 2
    for cost, a, b in path:
        # 3
        if find_parent(a) != find_parent(b):
            answer += cost
            if max_cost < cost:
                max_cost = cost
            union_parent(a, b)

    return answer - max_cost

if __name__ == "__main__":
    N, M = map(int, input().split())
    path = []
    for _ in range(M):
        a, b, w = map(int, input().split())
        path.append((w, a, b))

    print(solution(N, M, path))


'''
    알고리즘: 최소신장트리(프림 알고리즘)
    시간복잡도: O((M+N)logN + M) -> 약 천구백만
    Python: 통과 (6872 ms)
'''
import sys
import heapq

input = sys.stdin.readline

def solution(path):
    '''
        Prim Algorithm
        1. 임의의 정점을 선택
        2. 해당 정점에서 갈 수 있는 간선을 min heap에 넣는다.
        3. 최솟값을 뽑아 해당 정점을 방문하지 않았다면 선택한다.
    '''
    answer = 0
    max_cost = 0

    # 1번 정점부터 시작
    heap = [(0, 1)]
    visited = set()

    while heap:
        cost, dest = heapq.heappop(heap)

        if dest not in visited:
            visited.add(dest)
            answer += cost
            if max_cost < cost:
                max_cost = cost

            for way in path[dest]:
                if way[1] not in visited:
                    heapq.heappush(heap, way)
    
    # 마을을 두개로 구분하기 위해 최대 코스트 거리 제거
    return answer - max_cost

if __name__ == "__main__":
    N, M = map(int, input().split())
    path = {i+1:[] for i in range(N)}

    for _ in range(M):
        a, b, w = map(int, input().split())
        path[a].append((w, b))
        path[b].append((w, a))

    print(solution(path))