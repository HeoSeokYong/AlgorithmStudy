import sys
input = sys.stdin.readline

# 분할정복 & 행렬의 거듭제곱 활용
n = int(input())
p = 1000000007

# 행렬의 제곱을 구하는 분할 정복
def power(adj, n):
    if n==1:
        return adj
    elif n%2:
        return multi(power(adj, n-1), adj)
    else:
        return power(multi(adj, adj), n//2)

# 행렬의 곱셈
def multi(a,b):
    res = [[0] * len(b[0]) for _ in range(2)]
    for i in range(len(a)):
        for j in range(len(b[0])):
            tmp = 0
            for k in range(len(a)):
                tmp += a[i][k] * b[k][j]
            res[i][j] = tmp % p
    return res

# 초기 행렬
adj = [[1,1], [1,0]]
# 피보나치 초기값
start = [[1], [1]]

if n < 3:
    print(1)
else:
    print(multi(power(adj, n-2), start)[0][0])