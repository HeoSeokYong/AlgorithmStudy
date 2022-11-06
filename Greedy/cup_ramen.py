# 백준 #1781 컵라면
'''
    Algorithm: 그리디, 최소힙
    Time Complexity: O(NlogN)

    N 최대 200,000 -> NlogN 이하 필요
    문제들을 오름차순 정렬 후 heapq에 차례로 넣어줌. (뒤로갈수록 데드라인은 같거나 길어짐)
    그 때 heap의 길이가 현 문제의 데드라인보다 길어질 경우 가장 컵라면이 적은 값을 빼줌.
'''
import sys
import heapq

input = sys.stdin.readline

def solution(N):
    problems = [tuple(map(int, input().split())) for _ in range(N)]

    problems.sort()

    heap = []

    for prob in problems:
        heapq.heappush(heap, prob[1])
        if prob[0] < len(heap):
            heapq.heappop(heap)

    return sum(heap)


if __name__ == "__main__":
    N = int(input())

    print(solution(N))