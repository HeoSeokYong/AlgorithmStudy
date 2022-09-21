import sys
input = sys.stdin.readline

n = int(input())
xys = [list(map(int, input().split())) for _ in range(n)]

# x축 기준 정렬
xys.sort()

# 두 점 사이의 거리 구하는 함수 (제곱을 출력해야 하기때문에 제곱 그대로 반환)
def getDist(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def solution(start, end):
    # 점이 1개일 때
    if start == end:
        return float('inf')
    # 점이 2개 남았을 때
    if end-start == 1:
        return getDist(xys[start], xys[end])
    
    # 분할-정복
    mid = (start+end) // 2
    minDist = min(solution(start, mid), solution(mid, end))

    # x축을 기준으로 후보 점들을 찾는다.
    target = []
    for i in range(start, end+1):
        if (xys[mid][0] - xys[i][0])**2 < minDist:
            target.append(xys[i])
    
    # y축 기준 정렬
    target.sort(key=lambda x: x[1])

    # y축 기준으로 후보 점들 사이의 거리 비교
    l = len(target)
    for i in range(l-1):
        for j in range(i+1, l):
            if (target[i][1] - target[j][1]) ** 2 < minDist:
                minDist = min(minDist, getDist(target[i], target[j]))
            else:
                break
                # 현재 후보 점이 다음 점과 최소 거리보다 멀다면 더 볼 필요x
                # 이거 안하면 시간초과
    return minDist

print(solution(0, n-1))