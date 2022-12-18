# 백준 #
'''
    Algorithm: CCW
    Time Complexity: O(1)

'''
import sys

input = sys.stdin.readline

def CCW(p1: tuple, p2: tuple, p3:tuple) -> int:
    S = p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] \
        - (p1[0]*p3[1] + p2[0]*p1[1] + p3[0]*p2[1])
    
    if S > 0:
        return 1
    elif S < 0:
        return -1
    else:
        return 0
        

if __name__ == "__main__":
    points = [tuple(map(int, input().split())) for _ in range(3)]

    print(CCW(*points))