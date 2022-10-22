# 프로그래머스
import heapq

def find_min(anslist):
    comp_list = [sum([i*ans[i] for i in range(len(ans))]) for ans in anslist]
    return anslist[comp_list.index(max(comp_list))]

def solution(n, info):
    answer = []
    min_score = 1e5
    # 어피치의 점수
    apeach_score = sum([(10-i) if info[i] else 0 for i in range(len(info))])
    
    heap = [(apeach_score, [])]

    while heap:
        score, lion = heapq.heappop(heap)
        arrow = n - sum(lion)
        idx = len(lion)
        
        # 화살을 다 쓸 경우 기록
        if arrow == 0 or idx == len(info)-1:
            if arrow != 0:
                lion.append(arrow)
            if min_score > score:
                min_score = score
                answer = [lion]
            elif min_score == score:
                answer.append(lion)
            continue
        
        # 해당 점수를 고려하지 않는 경우
        heapq.heappush(heap, (score, lion + [0]))
        
        # 고려하는 경우 (화살 수가 충분할 때)
        if info[idx] < arrow:
            if info[idx] == 0:
                score -= (10-idx)
            else:
                score -= 2*(10-idx)
            heapq.heappush(heap, (score, lion + [info[idx] + 1]))

    if min_score >= 0:
        return [-1]
    else:
        answer = find_min(answer)
        while len(answer) < 11:
            answer.append(0)
            
        return answer