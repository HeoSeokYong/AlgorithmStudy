def where(N, r, c):
    tmp = [0]
    for i, n in enumerate(reversed(range(N))):
        comp = 2**(n)
        if c < comp:
            if r < comp:
                tmp.append(0)
            else:
                r -= comp
                tmp.append(2)
        else:
            c -= comp
            if r < comp:
                tmp.append(1)
            else:
                r -= comp
                tmp.append(3)           

    return tmp[1:]

want = input().split()
N, r, c = [int(_) for _ in want]
m = 0
tmp = where(N,r,c)
answer = 0

for t in reversed(tmp):
  answer += t * (2**m)
  m+=2

print(answer)