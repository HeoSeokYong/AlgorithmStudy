import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

def calc(nums):
    '''
        - nums의 길이가 1일 때: => A
        - nums의 길이가 2일 때: 
            - 두 수가 같을 경우: => 해당 수
            - 두 수가 다를 경우: => A
        - nums의 길이가 3이상일 때:
            (nums의 1, 2번째 원소를 확인)
            - nums의 인접한 두 수가 같을 때:
                - nums의 모든 수가 같을 경우: => 해당 수
                - 하나라도 다를 경우: => B
            - nums의 인접한 두 수가 다를 때:
                - a, b 값을 구함.
                    - a, b 모두 정수일 때:
                        - nums의 모든 수에 대해 패턴을 만족: => 다음 수 예측값
                        - nums의 하나라도 패턴을 만족 x: => B
                    - a, b 중 하나라도 정수 아닐 때: => B

    '''
    if len(nums) == 1:
        result = 'A'
    elif len(nums) == 2:
        if nums[0] != nums[1]:
            result = 'A'
        else:
            result = nums[0]
    else:
        if nums[1] == nums[0]:
            if len(set(nums)) == 1:
                result = nums[0]
            else:
                result = 'B'
        else:
            a = (nums[2] - nums[1]) / (nums[1] - nums[0])
            b = nums[1] - (nums[0] * a)

            if a.is_integer() and b.is_integer():
                for i in range(N-1):
                    if nums[i+1] != nums[i]*a + b:
                        return 'B'
                result = int((nums[-1]*a) + b)
            else:
                result = 'B'

    return result

print(calc(nums))