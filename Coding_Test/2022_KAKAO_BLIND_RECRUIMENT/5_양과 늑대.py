# 프로그래머스
'''
    이진 트리, 양 모으기
    해당 늑대가 막고 있는 양 
    해당 양을 얻기 위해 얻어야하는 늑대
    <미완>
'''
def solution(info, edges):
    answer = 0
    
    # 트리 만들기
    tree = {i:[] for i in range(len(info))}
    for a, b in edges:
        tree[a].append(b)
        
    # stack을 사용한 dfs를 통해 양과 늑대의 관계 갱신
    wolves = {} # 늑대들의 인덱스와 해당 늑대가 막고 있는 양 표시
    sheeps = {} # 양들의 인덱스와 해당 양을 얻기 위해 얻어야하는 늑대 표시
    
    for i in range(len(info)):
        if info[i] == 1:
            wolves[i] = set()
        else:
            sheeps[i] = set()

    stack = [(0, set())]
    
    while stack:
        cur, wolf_list = stack.pop()

        extraW = set()
        if info[cur] == 0: # 양
            # sheeps 와 wolves 갱신
            sheeps[cur] = wolf_list
            for wolf in wolf_list:
                wolves[wolf].add(cur)
            
        else: # 늑대
            extraW.add(cur)

        for nxt in tree[cur]:
            stack.append((nxt, wolf_list | extraW))

    # 양 모으기 시작
    sheep_cnt, wolf_cnt = 0, 0
    
    while True:
        get_sheep = [] # 얻을 수 있는 양
        consider_sheep = [] # 고민이 필요한 양
        
        for k in sheeps.keys():
            if not sheeps[k]:
                get_sheep.append(k)
            else:
                # 늑대를 얻고 양도 얻을 수 있는 경우
                if wolf_cnt + len(sheeps[k]) < sheep_cnt:
                    consider_sheep.append(k)
                        
        if not get_sheep and not consider_sheep:
            break
            
        if get_sheep:
            for k in get_sheep:
                del sheeps[k]
                sheep_cnt += 1
        
        if consider_sheep:
            max_w, pick = 0, 0
            for k in consider_sheep:
                sum_w = 0
                for w in sheeps[k]:
                    sum_w += len(wolves[w])
                if max_w < sum_w:
                    max_w = sum_w
                    pick = k
                    
            wolf_cnt += len(sheeps[pick])
            ws = sheeps.pop(pick)
            
            for w in ws:
                wolves[w].discard(pick)
                wp = wolves.pop(w)
                for s in wp:
                    sheeps[s].discard(w)
                        
            sheep_cnt += 1
        
        print(sheep_cnt, wolf_cnt)
        print(wolves)
        print(sheeps)
        
    return sheep_cnt

if __name__ == "__main__":
    info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
    edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]

    info2 = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
    edges2 = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]

    solution(info, edges)
    solution(info2, edges2)