# 백준 #1715 카드 정렬하기
'''
    Algorithm: heapq, greedy
    Time complexity: O(NlogN)
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