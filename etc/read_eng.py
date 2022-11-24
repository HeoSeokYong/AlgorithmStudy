# 백준 #1501 영어 읽기
'''
    Algorithm: 해시, 구현
    Time complexity: O(N + M)
'''
import sys

input = sys.stdin.readline

def solution(N, M, dict, sentence):
    dictionary = {}

    def get_morpheme(word):
        tmp = {}

        for i in range(1, len(word)-1):
            if word[i] not in tmp:
                tmp[word[i]] = 1
            else:
                tmp[word[i]] += 1

        name = []
        for k, v in sorted(tmp.items()):
            name.extend([k, v])

        return (word[0] + word[-1], "".join(list(map(str, name))))

    # 사전 분석
    for word in dict:
        if len(word) < 3:
            key = (word)
        else:
            key = get_morpheme(word)

        if key in dictionary:
            dictionary[key] += 1
        else:
            dictionary[key] = 1

    # 문장 분석
    for s in sentence:
        words = s.split()
        res = 1
        for word in words:
            if len(word) < 3:
                k = (word)
            else:
                k = get_morpheme(word)
            if k not in dictionary:
                res = 0
            else:
                res *= dictionary[k]

        print(res)

if __name__ == "__main__":
    N = int(input())
    dict = [input().rstrip() for _ in range(N)]
    M = int(input())
    sentence = [input().rstrip() for _ in range(M)]

    solution(N, M, dict, sentence)