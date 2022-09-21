'''
    움직일 수 있는 건 110 뿐
    생기는 110들을 전부 모아서 한번에 이동.
    110을 뺀 남은 문자열의 적절한 위치에 110들을 넣어 줌.
        맨 끝 0: 맨 뒤
        맨 끝 1: 맨 끝의 연속된 1들의 앞
'''

def move110(word):
    result = ''
    num110 = 0

    # 110을 뺀 문자열과 110의 개수 구하기
    for i in range(len(word)):
        if word[i] == '0' and result[-2:] == '11': # 110
            result = result[:-2] 
            num110 += 1
        else:
            result += word[i]

    # 남은 문자열의 맨 끝 정보 확인
    j = len(result) - 1
    
    while j >= 0:
        if result[j] == '1':
            j -= 1
        else:
            break

    return result[:j+1] + '110' * num110 + result[j+1:]

def solution(s):
    return [move110(word) for word in s]


if __name__ == "__main__":
    test_case = [["1110", "100111100", "0111111010"], ["00001", "11"], ["1100111011101001"]]
    answers = [["1101", "100110110", "0110110111"], ["00001", "11"], ["0101101101101101"]]
    
    for i in range(len(test_case)):
        print(test_case[i])
        print(solution(test_case[i]))
        print(answers[i])
        