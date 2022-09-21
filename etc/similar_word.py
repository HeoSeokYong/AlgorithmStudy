from copy import deepcopy

n = int(input())
answer = 0
base_word = input()
base_dict = {}

for b in base_word:
    if b in base_dict:
        base_dict[b] += 1
    else:
        base_dict[b] = 1

for i in range(n-1):
    word = input()
    dif = abs(len(base_word) - len(word))
    
    if dif <= 1:
        tmp = deepcopy(base_dict)
        cnt = 0
        
        for w in word:
            if w in tmp and tmp[w] > 0:
                tmp[w] -= 1
            else:
                cnt += 1
                
        if sum(tmp.values()) <= 1 and cnt <= 1:
            answer += 1

print(answer)