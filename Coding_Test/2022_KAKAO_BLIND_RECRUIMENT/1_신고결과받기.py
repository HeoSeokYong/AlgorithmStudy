# 프로그래머스 2022 카카오 공채 #1 신고결과받기
def solution(id_list, report, k):
    answer = {id: 0 for id in id_list}
    report_dict = {id: set() for id in id_list}
    
    for rep in report:
        # a: 신고한 사람, b: 신고받은 사람
        a, b = rep.split()
        
        # 해당 id를 신고한 id를 저장
        report_dict[b].add(a)

    for i in range(len(id_list)):
        id = id_list[i]
        
        if len(report_dict[id]) >= k:
            for x in report_dict[id]:
                answer[x] += 1
                
    return list(answer.values())