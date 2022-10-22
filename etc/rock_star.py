# 백준 #1581 락스타 락동호
'''
    Algorithm: 구현(분기)
    Time Complexity: O(1)
'''
import sys


input = sys.stdin.readline

def solution(ff, fs, sf, ss):
    result = 0
    if ff or fs:
        if ff:
            result += ff
        
        if fs:
            if fs > sf:
                result += 2*sf + 1
            else:
                result += 2*fs

            result += ss
    else:
        result += ss
        if sf:
            result += 1

    return result


if __name__ == "__main__":
    ff, fs, sf, ss = map(int, input().split())

    print(solution(ff, fs, sf, ss))