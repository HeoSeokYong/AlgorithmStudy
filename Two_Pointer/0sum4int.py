# 합이 0인 네 정수
import sys
input = sys.stdin.readline

n = int(input())
nums = {'A':[], 'B':[], 'C':[], 'D':[]}

for _ in range(n):
    a, b, c, d = map(int, input().split())
    nums['A'].append(a)
    nums['B'].append(b)
    nums['C'].append(c)
    nums['D'].append(d)

# a와 b, c와 d 각 모든 합의 경우의 수를 저장
ab, cd = [], []
for i in range(n):
    for j in range(n):
        ab.append(nums['A'][i] + nums['B'][j])
        cd.append(nums['C'][i] + nums['D'][j])
ab.sort()
cd.sort()

# 투 포인터
l = 0 # ab의 첫번째 
r = len(cd) - 1 # cd의 마지막
answer = 0

while l < len(ab) and r >= 0:
    nextl = l+1
    nextr = r-1

    # 중복 확인
    while nextl < len(ab) and ab[nextl] == ab[l]:
        nextl += 1
    while nextr >= 0 and cd[nextr] == cd[r]:
        nextr -= 1
    
    res = ab[l] + cd[r]
    if res == 0:
        answer += (nextl - l) * (r - nextr)
        l, r = nextl, nextr
    elif res > 0:
        r = nextr
    else: # res < 0
        l = nextl
    
print(answer)