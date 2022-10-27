# 프로그래머스 2021 카카오 채용연계형 인턴십 #1 숫자 문자열과 영단어
'''
    Algorithm: 구현
    Time Complexity: -
'''
def solution(s):
    nums = {'one':'1', 'two':'2', 'three':'3',
            'four':'4', 'five':'5', 'six':'6',
            'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}
    
    for n in nums.keys():
        s = s.replace(n, nums[n])

    return