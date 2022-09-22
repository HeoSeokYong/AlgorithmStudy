import sys
input = sys.stdin.readline

n = int(input())
link = [(i+1, int(x)) for i, x in enumerate(input().split())]

def is_twist(p1, p2):
    return p1[1] > p2[1]

def binary_search(left, right, target):
    while left < right:
        mid = (left + right) // 2

        if semiC[mid][1] < target:
            left = mid + 1
        else:
            right = mid

    return right

i = 1
semiC = [link[0]]

while i < n:
    # 꼬였을 경우 이분 탐색을 통해 반도체 리스트의 적합한 위치에 저장
    if is_twist(semiC[-1], link[i]):
        idx = binary_search(0, len(semiC), link[i][1])
        semiC[idx] = link[i]
    # 꼬이지 않았을 경우 반도체 리스트에 추가
    else:
        semiC.append(link[i])
    i += 1

print(len(semiC))