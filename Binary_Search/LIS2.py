import sys 
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
tmp = [0]

for i in range(n):
    if tmp[-1] < num_list[i]:
        tmp.append(num_list[i])
    else:
        left = 0
        right = len(tmp)
        
        while left < right:
            mid = (left+right)//2
            if tmp[mid] < num_list[i]:
                left = mid+1
            else:
                right = mid
        tmp[right] = num_list[i]
        
print(len(tmp)-1)