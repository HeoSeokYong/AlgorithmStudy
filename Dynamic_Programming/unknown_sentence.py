# 백준 #1099 알 수 없는 문장
'''
    Algorithm: dp
    Time Complexity: O(SNW) (S: 문장의 길이, W: 단어의 길이)

    dfs -> 시간초과
    dp로 풀어야겠다.
'''
import sys

input = sys.stdin.readline
INF = sys.maxsize

def solution(sentence, N, words):
    dp = [0] + [INF for _ in range(len(sentence))]
    
    def is_same(w1, w2):
        ''' 두 문자열의 구성요소가 같은 지 확인하는 함수 '''
        return sorted(w1) == sorted(w2)

    def get_cost(w1, w2):
        ''' 해당 문자의 비용을 반환 '''
        cost = 0
        for a, b in zip(w1, w2):
            if a != b:
                cost += 1
        return cost

    for idx in range(len(sentence)):
        for word in words:
            target = sentence[idx:idx+len(word)]
            if is_same(word, target):
                cost = get_cost(word, target)
                dp[idx + len(word)] = min(dp[idx + len(word)], dp[idx] + cost)

    if dp[-1] == INF:
        return -1
    else:
        return dp[-1]


if __name__ == "__main__":
    sentence = input().rstrip()
    N = int(input())
    words = [input().rstrip() for _ in range(N)]

    print(solution(sentence, N, words))