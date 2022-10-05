# # 백준 #2610 회의 준비
'''
    Algorithm: 큐
    시간복잡도: O(N^2)?
'''

import sys
from collections import deque

input = sys.stdin.readline
INF = 1e2

def friends_committee(friends):
    '''
        참석자들로 위원회를 만들고 리턴
    '''
    committees = []
    belong = [False] * (len(friends)+1)  

    for i in range(1, len(friends)+1):
        deq = deque()
        comm = set()

        if not belong[i]:
            deq.append(i)
            belong[i] = True

            while deq:
                x = deq.popleft()
                comm.add(x)

                for friend in friends[x]:
                    if not belong[friend]:
                        belong[friend] = True
                        deq.append(friend)

            committees.append(comm)

    return committees

def elect_representative(friends, committee):
    '''
        모든 참석자들의 의사전달시간 중 최댓값이 최소가 되도록 대표를 정함
    '''
    time = INF
    representative = 0

    for c in committee:
        cmt_dict = {cmt: [False, 0] for cmt in committee}

        deq = deque([(c, 0)])
        cmt_dict[c][0] = True
        
        while deq:
            x, t = deq.popleft()

            for friend in friends[x]:
                if not cmt_dict[friend][0]:
                    cmt_dict[friend][1] = t+1
                    cmt_dict[friend][0] = True
                    deq.append((friend, t+1))
        
        max_comm_time = max(cmt_dict.values(), key=lambda x:x[1])[1]
        if time > max_comm_time:
            time = max_comm_time
            representative = c

    return representative

def solution(friends):
    committees = friends_committee(friends)
    return sorted([elect_representative(friends, committee) for committee in committees])


if __name__ == "__main__":
    N = int(input())
    M = int(input())

    friends = {i: [] for i in range(1, N+1)}
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)

    K = solution(friends)

    print(len(K))
    for k in K:
        print(k)

### **************************************************************

'''
    Algorithm: 플로이드-워셜 
    시간복잡도: O(N^3) = 약 1,000,000 
'''

import sys

input = sys.stdin.readline
INF = 1e2

def floyd_warshall(N, friends):
    dist = [[INF] * (N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        dist[i][i] = 0
    
    for i in range(1, N+1):
        for j in friends[i]:
            dist[i][j] = 1
    
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def friends_committee(dist):
    '''
        참석자들로 위원회를 만들고 리턴
    '''
    committees = []
    belong = [False] * (len(dist))  

    for i in range(1, len(dist)):
        comm = []
        if not belong[i]:
            for j in range(1, len(dist)):
                if dist[i][j] != INF:
                    belong[j] = True
                    comm.append(j)

            committees.append(comm)

    return committees

def elect_representative(dist, committee):
    '''
        모든 참석자들의 의사전달시간 중 최댓값이 최소가 되도록 대표를 정함
    '''
    time = INF
    representative = 0

    for c in committee:
        max_comm_time = max([d for d in dist[c] if d < INF])
        if time > max_comm_time:
            time = max_comm_time
            representative = c
    
    return representative

def solution(N, friends):
    dist = floyd_warshall(N, friends)
    committees = friends_committee(dist)
    
    return sorted([elect_representative(dist, committee) for committee in committees])


if __name__ == "__main__":
    N = int(input())
    M = int(input())

    friends = {i: [] for i in range(1, N+1)}
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)

    K = solution(N, friends)

    print(len(K))
    for k in K:
        print(k)