# 프로그래머스
def transfer_k(n, k):
    result = ''
    
    while n > 0:
        n, mod = divmod(n, k)
        result += str(mod)
    
    return result[::-1]

def is_prime(x):
    x = int(x)
    
    if x == 1:
        return False
    
    for i in range(2, int(x**(1/2) + 1)):
        if x % i == 0:
            return False
        
    return True

def solution(n, k):
    answer = 0
    k_num = transfer_k(n, k)
    num_list = [n for n in k_num.split('0') if n]
    
    for num in num_list:
        if is_prime(num):
            answer += 1
    
    return answer