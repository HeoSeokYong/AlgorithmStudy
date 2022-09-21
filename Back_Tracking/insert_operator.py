import sys
input = sys.stdin.readline
''' list는 전역변수이다. '''

len_list = int(input())
num_list = list(map(int, input().split()))

opr_ = ['+','-','*','/']
opr = list(map(int, input().split()))

max_min = [float('-inf'), float('inf')]

def dfs(cnt, res):
    if cnt == len(num_list): # 종료
        max_min[0] = max(max_min[0], res)
        max_min[1] = min(max_min[1], res)
        return
    
    for i in range(4):
        if opr[i] > 0:
            opr[i] -= 1
            dfs(cnt+1, int(eval(str(res)+opr_[i]+str(num_list[cnt]))))
            opr[i] += 1


dfs(1, num_list[0])

print(max_min[0])
print(max_min[1])