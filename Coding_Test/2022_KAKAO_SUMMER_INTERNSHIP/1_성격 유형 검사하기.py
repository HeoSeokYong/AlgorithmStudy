# 프로그래머스
def solution(survey, choices):
    # 왼쪽 문자는 - 오른쪽 문자는 + 점수를 더하여 계산
    score = [0] * 4
    kbti = ['RT', 'CF', 'JM', 'AN']
    
    for i in range(len(survey)):
        if choices[i] > 4: # 오른쪽이 점수 얻는 경우
            category = survey[i][1]
        elif choices[i] < 4: # 왼쪽이 점수 얻는 경우
            category = survey[i][0]
        else: 
            continue
        
        sco = abs(choices[i] - 4)
        
        for j in range(len(kbti)):
            if category in kbti[j]:
                if category == kbti[j][0]: # 왼쪽 문자일 경우 -
                    score[j] -= sco
                else: # 오른쪽 문자일 경우 +
                    score[j] += sco
                break
    
    answer = []
    for i in range(4):
        if score[i] > 0:
            answer.append(kbti[i][1])
        else:
            answer.append(kbti[i][0])
            
    
    return "".join(answer)