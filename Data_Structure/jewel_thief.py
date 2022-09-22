'''
    K개의 가방, 가방에는 최대 1개의 보석
    용량이 작은 가방부터 담을 수 있는 모든 보석을 heap에 넣는다.
    그 중 value가 가장 큰 것을 가져 간다.
    heap이 비었으면 pass.
'''
import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

jewelry = []
for i in range(N):
    m, v = map(int, input().split())
    heapq.heappush(jewelry, (m, v))

bag_list = [int(input()) for _ in range(K)]
bag_list.sort()

def thief(jewelry, bag_list):
    answer = 0
    heap = []

    for bag in bag_list:
        while jewelry and jewelry[0][0] <= bag:
            heapq.heappush(heap, -heapq.heappop(jewelry)[1])
        if heap:
            answer -= heapq.heappop(heap)

    return answer

print(thief(jewelry, bag_list))
