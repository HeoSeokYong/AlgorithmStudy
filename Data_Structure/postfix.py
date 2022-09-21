import sys
from collections import deque
input = sys.stdin.readline

answer = ''
x = input()
stack = deque()

for s in x:
    if s.isalpha():
        answer += s
    else:
        if s == '(':
            stack.append(s)
        elif s in '*/':
            while len(stack) and stack[-1] in '*/':
                answer += stack.pop()
            stack.append(s)
        elif s in '+-':
            while len(stack) and stack[-1] != '(':
                answer += stack.pop()
            stack.append(s)
        elif s == ')':
            while stack[-1] != '(':
                answer += stack.pop()
            stack.pop()
while len(stack):
    answer += stack.pop()

print(answer)