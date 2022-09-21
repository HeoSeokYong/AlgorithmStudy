print(eval('-'.join([str(eval("+".join([str(int(j)) for j in i.split('+')]))) for i in input().split('-')])))
