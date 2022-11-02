# 프로그래머스 2021 카카오 채용연계형 인턴십 #4 미로 탈출
'''
    Algorithm: 다익스트라, 비트마스킹
    Time Complexity: O(N * T * 2^T * logN)
'''
import heapq

def solution(n, start, end, roads, traps):
    path = {i+1: [] for i in range(n)}
    trap_dict = {trap: idx for idx, trap in enumerate(traps)}
    visited = [[False] * (n+1) for _ in range(1 << len(traps))]
 
    # True: 역방향, False: 정방향
    for p, q, s in roads:
        path[p].append((q, s, False))
        path[q].append((p, s, True))

    # (시간, 노드, 함정발동상태)
    heap = [(0, start, 0)]

    while heap:
        time, node, state = heapq.heappop(heap)

        if node == end:
            return time

        if visited[state][node]:
            continue
        else:
            visited[state][node] = True

        for dist, t, type in path[node]:
            nstate = state
            
            cur_isTrap = True if node in trap_dict else False
            dist_isTrap = True if dist in trap_dict else False

            # isTrapOn : 현재 경로에 함정이 반영되어 있는지 
            if not cur_isTrap and not dist_isTrap:
                isTrapOn = False

            elif cur_isTrap ^ dist_isTrap:
                n = node if cur_isTrap else dist
                isTrapOn = ((1 << trap_dict[n]) & state) >> trap_dict[n]

            else: # cur_isTrap and dist_isTrap
                isTrapOn = (((1 << trap_dict[node]) & state) >> trap_dict[node]) ^ (((1 << trap_dict[dist]) & state) >> trap_dict[dist])
            
            if type != isTrapOn:
                continue
            
            if dist_isTrap:
                nstate = state ^ (1 << trap_dict[dist])
            
            heapq.heappush(heap, (time + t, dist, nstate))


if __name__ == "__main__":
    probs = [[3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]], [	4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]]]

    for a,b,c,d,e in probs:
        print(solution(a,b,c,d,e))


# 예전에 구현했던 코드
'''
import heapq

def solution(n, start, end, roads, traps):
    q = []
    start -= 1; end -= 1
    graph = [[] for _ in range(n)]
    trap_dict = {trap-1:idx for idx, trap in enumerate(traps)} # 각 트랩 발동 여부 확인
    visited = [[False]*n for _ in range(1<<len(traps))]
    heapq.heappush(q, [0, start, 0])
    
    for s, e, c in roads:
        graph[s-1].append([e-1, c, 0]) # 0: 정방향
        graph[e-1].append([s-1, c, 1]) # 1: 역방향

    while q:
        cost, node, state = heapq.heappop(q)
        if node == end:
            return cost
        if visited[state][node] == True:
            continue
        else:
            visited[state][node] = True
        
        for nnode, ncost, ntype in graph[node]:
            nstate = state
            
            cur_isTrap = True if node in trap_dict else False;
            next_isTrap = True if nnode in trap_dict else False;
            
            if not cur_isTrap and not next_isTrap:
                if ntype == 1: # trap이 아닌데 역방향
                    continue
            elif cur_isTrap ^ next_isTrap:
                n = node if cur_isTrap else nnode
                isTrapOn = (state & (1<<trap_dict[n]))>>trap_dict[n]
                if isTrapOn != ntype: # trap인데 정방향
                    continue
            else: # 둘다 trap
                isTrapOn = (state & (1<<trap_dict[node]))>>trap_dict[node] # 현재 trap이 on인지
                n_isTrapOn = (state & (1<<trap_dict[nnode]))>>trap_dict[nnode] # 다음 trap이 on인지
                if (isTrapOn ^ n_isTrapOn) != ntype: # 하나만 on일 때 1(역) else 0(정)
                    continue
            if next_isTrap:
                nstate = state ^ (1<<trap_dict[nnode]) # nnode trap을 on/off
                
            heapq.heappush(q, (cost+ncost, nnode, nstate))
'''