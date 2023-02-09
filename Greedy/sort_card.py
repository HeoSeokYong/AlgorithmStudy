# 백준 #1715 카드 정렬하기
'''
    Algorithm: greedy, 우선순위큐
    Time Complexity: O(NlogN)

    2023.02.09 풀이
'''
import sys
import heapq
from typing import List, Tuple, Callable

def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    cards = [int(input()) for _ in range(N)]
    return N, cards


def solution(N:int, cards:List[int]) -> int:
    result = 0
    heapq.heapify(cards)

    while len(cards) > 1:
        summ = heapq.heappop(cards) + heapq.heappop(cards)
        result += summ
        heapq.heappush(cards, summ)

    return result


if __name__ == "__main__":
    print(solution(*read_data()))


'''
    Algorithm: heapq, greedy
    Time complexity: O(NlogN)

    2022.10.27 풀이
'''
import sys
import heapq

input = sys.stdin.readline

def solution(N, cards):
    result = 0
    card_deck = []

    heapq.heapify(cards)
    
    while cards:
        if len(card_deck) == 2:
            result += sum(card_deck)
            heapq.heappush(cards, sum(card_deck))
            card_deck = []

        else:
            card_deck.append(heapq.heappop(cards))

    if len(card_deck) == 2:
        result += sum(card_deck)
    return result


if __name__ == "__main__":
    N = int(input())
    cards = [int(input()) for _ in range(N)]

    print(solution(N, cards))