# 백준 #14890 경사로
'''
    Algorithm: 구현
    Time Complexity: O(N^2)
'''
import sys

input = sys.stdin.readline

def solution(N, L, maps):
    answer = 0
    
    def map_split(maps):
        ''' 맵을 가로 길과 세로 길로 나누어 반환 '''
        w_road, h_road = [], []

        for i in range(N):
            w_tmp, h_tmp = [], []
            for j in range(N):
                w_tmp.append(maps[i][j])
                h_tmp.append(maps[j][i])
            
            w_road.append(w_tmp)
            h_road.append(h_tmp)

        return w_road, h_road
                
    def analyze_road(road):
        ''' 길을 연속된 부분끼리 묵어 반환 '''
        result = []
        tmp = [road[0], 0]
        for r in road:
            if r == tmp[0]:
                tmp[1] += 1
            else:
                result.append(tmp)
                tmp = [r, 1]

        result.append(tmp)
        return result

    w_road, h_road = map_split(maps)

    # w road
    for w in w_road:
        ar = analyze_road(w)
        score = 1
        
        for i in range(len(ar)-1):
            if ar[i][0] == ar[i+1][0] - 1 and ar[i][1] >= L:
                ar[i][1] -= L
            elif ar[i][0] == ar[i+1][0] + 1 and ar[i+1][1] >= L:
                ar[i+1][1] -= L
            else:
                score = 0
                break

        answer += score
        
    # h road
    for h in h_road:
        ar = analyze_road(h)
        score = 1
        
        for i in range(len(ar)-1):
            if ar[i][0] == ar[i+1][0] - 1 and ar[i][1] >= L:
                ar[i][1] -= L
            elif ar[i][0] == ar[i+1][0] + 1 and ar[i+1][1] >= L:
                ar[i+1][1] -= L
            else:
                score = 0
                break

        answer += score

    return answer


if __name__ == "__main__":
    N, L = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]

    print(solution(N, L, maps))