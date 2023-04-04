# 백준 #9466 텀 프로젝트
'''
    Algorithm: dfs
    Time Complexity: O(N)

'''
import sys
from typing import List, Tuple, Callable


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    students = [0] + list(map(int, input().split()))

    return N, students


def solution(N:int, students:List[int]) -> int:
    result = N
    visited = [0 for _ in range(N+1)]

    for i in range(1, N+1):
        if not visited[i]:
            group = [i]
            visited[i] = i
            cur = i
            
            while not visited[students[cur]]:
                group.append(students[cur])
                visited[students[cur]] = i
                cur = students[cur]
            
            if visited[students[cur]] == i:
                while group.pop() != students[cur]:
                    result -= 1
                result -= 1

    return result


if __name__ == "__main__":
    T = int(input())
    
    for _ in range(T):
        print(solution(*read_data()))
