# 백준 #1339 단어 수학
'''
    Algorithm: greedy
    Time Complexity: O(NW) (W : 단어의 길이) 
    
    알파벳 별로 dictionary에 10 ** (해당 알파벳의 현재 자릿수) 를 더한 값을 저장한다.
    이후 값을 기준으로 내림차순 정렬 후 순서대로 9~0까지 부여하고 더해 결과값을 구한다.
'''
import sys
from collections import defaultdict
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    words = [input() for _ in range(N)]
    return N, words


def solution(N: int, words: List[str]) -> int:
    word_dict = defaultdict(int)

    for word in words:
        lev = len(word) - 1

        for i in range(len(word)):
            word_dict[word[i]] += (10 ** (lev-i))

    return sum(word_dict[k] * num for k, num in zip(sorted(word_dict.keys(), key=lambda x:word_dict[x], reverse=True), range(9, -1, -1)))


if __name__ == "__main__":
    print(solution(*read_data()))