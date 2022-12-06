# 백준 #1662 압축
'''
    Algorithm: 스택
    Time Complexity: O(N)

    try 1) 재귀 형식으로 해보자.
        - 잘 안된다..

    try 2) 스택으로 해보자.
        일반 숫자는 1로 넣고 ( 는 그대로 stack에 넣음
        ( 의 직전 숫자는 1이 아닌 숫자 그대로를 넣음
        )가 나왔을 경우 (가 나올때까지 pop하며 괄호 안 숫자의 개수와 괄호 
        숫자의 곱을 넣어줌
        
'''
import sys

input = sys.stdin.readline

def solution(S):
    stack = []

    for i in range(len(S)):
        if S[i] == '(':
            stack.pop()
            stack.append(int(S[i-1]))
            stack.append(S[i])

        elif S[i].isdigit():
            stack.append(1)

        else: # ')'
            s = 0
            while len(stack) and stack[-1] != '(':
                s += stack.pop()

            stack.pop() # ( pop
            stack.append(int(stack.pop()) * s)

    return sum(stack)


if __name__ == "__main__":
    S = input().rstrip()

    print(solution(S))