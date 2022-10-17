# 백준 #3980 선발 명단
'''
    dfs로 가능한 모든 경우를 조사하는데
    이미 선택한 선수, 포지션을 제외시켜 경우의 수를 줄임(백트래킹)
    알고리즘: dfs, 백트래킹
    시간복잡도: brute-force의 경우 -> O(5^11) = 약 4,800만
'''
import sys
from collections import deque

input = sys.stdin.readline

def solution(players):
    answer = 0
    stack = deque([([], set())])

    while stack:
        stat_list, player_set = stack.pop()

        for i in range(11):
            if i not in player_set and players[i][len(stat_list)] > 0:
                if len(stat_list) == 10:
                    answer = max(answer, sum(stat_list) + players[i][len(stat_list)])
                    continue
                stack.append((stat_list + [players[i][len(stat_list)]], player_set.union({i})))

    return answer

if __name__ == "__main__":
    for test_case in range(int(input())):
        players = [list(map(int, input().split())) for _ in range(11)]
        print(solution(players))