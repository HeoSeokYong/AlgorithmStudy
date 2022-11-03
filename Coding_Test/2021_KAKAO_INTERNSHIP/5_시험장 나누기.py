# 프로그래머스 2021 카카오 채용연계형 인턴십 #5 시험장 나누기
'''
    Algorithm: parametric search, dp
    Time Complexity: 

    최적화 문제 Q. 그룹을 k이하의 개수로 나눌때 얻을 수 있는 최소한의 최대 그룹 크기는 얼마인가?
    결정 문제 -> 그룹을 k 이하의 개수로 나눌 때 최대 그룹의 크기가 L 이하로 할 수 있나?
    L의 범위: (최소)모든 가중치의 합/k <= L <= 모든 가중치의 합

    dp[i][0] = i번 노드를 루트 노드로 하는 서브트리를 최대 그룹 인원이 L 이하가 되도록 하는 최소 그룹의 수
    dp[i][1] = i번 노드를 루트 노드로 하는 서브트리를 최대 그룹 인원이 L 이하가 되도록 dp[i][0]개로 나누었을 때,
               i번 노드가 포함되는 서브트리의 가중치 합의 최솟값

'''
def solution(k, num, links):
    N = len(num)
    MAX_L = sum(num)
    MIN_L = MAX_L // k

    room = {i: {'num': num[i], 'child': [], 'parent': -1} for i in range(len(num))}

    for i in range(N):
        for child in links[i]:
            if child != -1:
                room[i]['child'].append(child)
                room[child]['parent'] = i
    


    def check(L):
        res = 0
        # dp 활용
        dp = [[0, 0] for _ in range(N)]

        for i in range(N):
            
        


        return res < k
    
    def binary_search(l, r):
        while l < r:
            mid = (l + r) // 2

            if check(mid):
                l = mid + 1
            else:
                r = mid

        return r

    return binary_search(MIN_L, MAX_L)


if __name__ == "__main__":
    probs = [[3, [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1], [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]]]
    probs.append([1, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]])
    probs.append([2, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]])
    probs.append([4, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]])

    for a,b,c in probs:
        print(solution(a,b,c))