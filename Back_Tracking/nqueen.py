n = int(input())
cnt = 0
table = [0] * n

def promising(x):
    for i in range(x):
        if table[i] == table[x] or abs(i - x) == abs(table[i] - table[x]):
            return False
    return True

def nqueen(idx):
    if idx == len(table):
        global cnt
        cnt += 1
        return
    else:
        for i in range(len(table)):
            table[idx] = i
            if promising(idx):
                nqueen(idx+1)

nqueen(0)
print(cnt)