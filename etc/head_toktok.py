# 백준 #1241 머리 톡톡
'''
    Algorithm: 구현, 수학
    Time Complexity: O(N * sqrt(N))

    학생들의 번호를 카운팅 하고 
    각 번호의 약수에 해당하는 수의 개수를 더해주는 방식.
'''
import sys

input = sys.stdin.readline

def solution(N):
    students = [int(input()) for _ in range(N)]
    st_dict = dict()
    toktok = [0 for _ in range(N)]

    def get_divisor(n):
        divisorsList = []

        for i in range(1, int(n**(1/2)) + 1):
            if n % i == 0:
                divisorsList.append(i) 
                if (i ** 2) != n : 
                    divisorsList.append(n // i)

        return divisorsList

    for i in range(N):
        if students[i] in st_dict:
            st_dict[students[i]] += 1
        else:
            st_dict[students[i]] = 1

    for i in range(N):
        k = students[i]
        for d in get_divisor(k):
            if d in st_dict:
                if d == k:
                    toktok[i] -= 1
                toktok[i] += st_dict[d]

    return toktok


if __name__ == "__main__":
    N = int(input())

    print(*solution(N), sep='\n')