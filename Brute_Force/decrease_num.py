# 백준 #1038 감소하는 수
'''
    N <= 1000000
    시간복잡도: O(N)
'''
import sys

input = sys.stdin.readline

def solution(N):
    if N > 1022: # 감소하는 수의 최대 값인 9876543210이 나오는 시점
        return -1

    result = [0]
    
    while N:
        lev = 0
        result[lev] += 1
        
        # 감소하는 형태로 만들기
        while lev < len(result)-1 and result[lev] == result[lev+1]:
            result[lev] = lev
            result[lev+1] += 1
            lev += 1

        # 자릿수 증가
        if result[-1] == 10:
            while lev < len(result):
                result[lev] = lev
                lev += 1
            result.append(lev)
        
        N -= 1
        
    return sum(d * 10**i for i, d in enumerate(result))


if __name__ == "__main__":
    N = int(input())
    print(solution(N))
