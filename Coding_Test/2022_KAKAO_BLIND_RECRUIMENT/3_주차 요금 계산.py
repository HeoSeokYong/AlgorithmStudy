def cal_time(t1, t2):
    h1, m1 = map(int, t1.split(':'))
    h2, m2 = map(int, t2.split(':'))
    
    return (60*h2 + m2) - (60*h1 + m1)

def solution(fees, records):
    answer = {}
    parking = {}
    
    # 주차 정보 기록   
    for record in records:
        t, num, io = record.split()
        
        if num not in parking:
            answer[num] = {'time': 0, 'fee':0}
            parking[num] = {'IN': [], 'OUT': []}
            
        parking[num][io].append(t)
    
    # 주차 시간 누적
    for k in parking.keys():
        parking[k]['OUT'].append('23:59') # 출차 내역 없을 경우를 처리

        for i in range(len(parking[k]['IN'])):
            answer[k]['time'] += cal_time(parking[k]['IN'][i], parking[k]['OUT'][i])
            
        # 기본 시간
        answer[k]['fee'] += fees[1]

        # 시간 확인
        if answer[k]['time'] > fees[0]:
            answer[k]['time'] -= fees[0]

            d, m = divmod(answer[k]['time'], fees[2])
            if m != 0:
                d += 1
            answer[k]['fee'] += d * fees[3]
                
                
    return [answer[k]['fee'] for k in sorted(list(answer.keys()))]