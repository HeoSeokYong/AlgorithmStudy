'''
    알고리즘: 다익스트라

    출입구, 쉼터, 산봉우리
    쉼터, 산봉우리는 휴식 가능
    휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 해당 등산코스의 intensity
    출입구 중 한 곳에서 출발,
    산봉우리 중 한 곳만 방문한 뒤 원래 출입구로 복귀하는 코스
    등산코스에서 출입구는 처음과 끝에 한 번씩, 산봉우리는 한 번만 포함되어야 합니다.
    이러한 규칙을 지키면서 intensity가 최소가 되도록 등산코스
'''
import heapq

INF = float('inf')

def solution(n, paths, gates, summits):
    path_dict = {i+1:[] for i in range(n)}

    summits = set(summits)

    for i, j, w in paths:
        path_dict[i].append((w, j))
        path_dict[j].append((w, i))

    ''' 경로는 출발지 -> 도착지 까지이므로 중간에 들릴 곳은 쉼터 뿐이다. '''
    heap = [] # 현재 경로의 (최대 intensity, 현위치)
    dp = [INF] * (n+1)
    
    for gate in gates:
        dp[gate] = 0
        for w, d in path_dict[gate]:
            if dp[d] > w:
                dp[d] = w
                heapq.heappush(heap, (w, d))
        
    while heap:
        maxI, curNode = heapq.heappop(heap)
        
        if dp[curNode] < maxI:
            continue
        
        if curNode in summits:
            continue

        for w, d in path_dict[curNode]:
            if dp[d] > max(maxI, w):
                dp[d] = max(maxI, w)
                heapq.heappush(heap, (max(maxI, w), d))

    return min([[dp[summit], summit] for summit in summits])[::-1]


if __name__ == "__main__":
    cases = [[6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]],
    [7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]],
    [7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]],
    [5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]]]

    for a, b, c, d in cases:
        print(solution(a,b,c,d))