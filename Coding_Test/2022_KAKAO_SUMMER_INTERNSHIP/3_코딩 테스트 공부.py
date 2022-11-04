# 프로그래머스 2022 카카오 채용연계형 여름 인턴십 #3 코딩 테스트 공부
'''
    알고리즘: 다익스트라 with heapq
'''
import heapq

def max_alp(problems):
    return max(problems, key=lambda x:x[0])[0]

def max_cop(problems):
    return max(problems, key=lambda x:x[1])[1]

def solution(alp, cop, problems):
    answer = -1
    target_alp = max(alp, max_alp(problems))
    target_cop = max(cop, max_cop(problems))

    # 1초 소모해서 alp, cod +1
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])
    
    heap = [(0, alp, cop)]
    visited = set()
    
    while heap:
        time, cur_al, cur_co = heapq.heappop(heap)
        cur_al = min(cur_al, target_alp)
        cur_co = min(cur_co, target_cop)
        cur_node = (cur_al, cur_co)

        if cur_node in visited:
            continue
        
        visited.add(cur_node)

        if cur_al >= target_alp and cur_co >= target_cop:
            answer = time
            break

        for prob in problems:
            # 문제를 풀 수 있고, 단순 시간당 1 증가보다 효율이 같거나 좋을 때만 넣는다.
            if prob[0] <= cur_al and prob[1] <= cur_co and prob[2] + prob[3] >= prob[4]:
                heapq.heappush(heap, (time + prob[4], cur_al + prob[2], cur_co + prob[3]))
                    
    return answer

if __name__ == "__main__":
    print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
    print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))

# '''
#     주어진 모든 문제들을 풀 수있는 알고력과 코딩력을 얻는 최단시간
#     problems의 원소는 [필요 알고력, 필요 코딩렬, 보상 알고, 보상 코딩, 푸는 시간]
#     알고리즘: 자료구조 최소힙 -> 시간초과
#     ---> visited를 사용해 시간을 줄여야 했다
# '''
# import heapq

# def solution(alp, cop, problems):
#     answer = 0
#     prob_able = []
#     target_alp = max(problems, key=lambda x:x[0])[0]
#     target_cop = max(problems, key=lambda x:x[1])[1]
    
#     heap = [(0, -alp, -cop)]
    
#     while heap:
#         t, al, co = heapq.heappop(heap)
#         al, co = -al, -co
        
#         if al >= target_alp and co >= target_cop:
#             answer = t
#             break
        
#         for prob in problems:
#             # 풀 수 있는 경우 푼 경우를 heap에 추가
#             if al >= prob[0] and co >= prob[1]:
#                 if prob[2] + prob[3] > prob[4]: # 보상이 단순 시간 증가보다 좋을 경우
#                     heapq.heappush(heap, (t + prob[4], -(al + prob[2]), -(co + prob[3])))
#             # 못 푸는 경우 필요한 알고력과 코딩력을 얻기 위한 시간을 더하고 heap에 넣는다.
#             else:
#                 at, ct = 0, 0
#                 if al < prob[0]:
#                     at = prob[0] - al
#                 if co < prob[1]:
#                     ct = prob[1] - co
                    
#                 heapq.heappush(heap, (t+at+ct, -(al + at), -(co + ct)))
            
#     return answer
