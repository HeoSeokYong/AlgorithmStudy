# 프로그래머스 2021 카카오 채용연계형 인턴십 #3 표 편집
'''
    Algorithm: Fenwick Tree 
    Time Complexity: O((logN)^2)
'''
class FenwickTree:
    def __init__(self, n, k):
        self.graph = [1] * n
        self.tree = [0] * (n+1)
        self.k = k + 1
        self.recycle_bin = []

    def update(self, index, data):
        ''' 연관되어있는 모든 위치를 update '''
        while index < len(self.tree):
            self.tree[index] += data
            index += (index & - index) # 2진수로 했을 때 마지막 1의 위치
    
    def sum(self, index):
        ''' 해당 인덱스까지의 구간 합 구하기 '''
        ans = 0
        while index > 0:
            ans += self.tree[index]
            index -= (index & -index)

        return ans

    def binary_search(self, l, r, data):
        data += self.sum(self.k)

        ''' l ~ r 사이 범위에서 data의 구간합을 가지는 인덱스 리턴 '''
        while l < r:
            mid = (l+r) // 2

            if self.sum(mid) < data:
                l = mid + 1
            else:
                r = mid

        self.k = r

    def command(self, comm):
        com = comm.split()
        if com[0] == 'D':
            self.binary_search(self.k, len(self.tree)-1, int(com[1]))
        
        elif com[0] == 'U':
            self.binary_search(1, self.k, -int(com[1]))
        
        elif com[0] == 'C':
            self.recycle_bin.append(self.k)
            self.update(self.k, -1)
            self.graph[self.k-1] = 0
            # 제일 끝 1을 삭제한 경우
            if self.sum(self.k) == self.tree[-1]:
                self.binary_search(1, len(self.tree)-1, 0)
            else:
                self.binary_search(self.k, len(self.tree)-1, 1)

        elif com[0] == 'Z':
            idx = self.recycle_bin.pop()
            self.update(idx, 1)
            self.graph[idx-1] = 1
    
    def get_ox(self):
        return "".join(['O' if x == 1 else 'X' for x in self.graph])

def solution(n, k, cmd):
    fenwick = FenwickTree(n, k)

    for i in range(n):
        fenwick.update(i+1, 1)

    for c in cmd:
        fenwick.command(c)

    return fenwick.get_ox()

if __name__ == "__main__":
    print(solution(	8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))


''' 이전에 풀었던 코드 (linked list)
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class linkedlist:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.cur = self.head
        self.len = 1
        self.delq = deque()

    def append(self, data):
        self.cur.next = Node(data)
        self.tail = self.cur.next
        self.tail.prev = self.cur
        self.cur = self.cur.next
        self.len += 1

    def set_cur(self, index):
        self.cur = self.head
        while index:
            self.cur = self.cur.next
            index-=1

    def move(self, flag, step):
        if flag == 'U':
            while step:
                self.cur = self.cur.prev
                step-=1
        elif flag == 'D':
            while step:
                self.cur = self.cur.next
                step-=1

    def delete(self):
        self.delq.append(self.cur)
        self.len -= 1
        if self.cur == self.tail:
            self.cur = self.cur.prev
            self.cur.next = None
            self.tail = self.cur
        elif self.cur == self.head:
            self.cur = self.cur.next
            self.cur.prev = None
            self.head = self.cur
        else:
            pre = self.cur.prev
            nex = self.cur.next
            pre.next = nex
            nex.prev = pre
            self.cur = self.cur.next

    def ctrlz(self):
        self.len += 1
        node = self.delq.pop()
        if node.prev is not None:
            pre = node.prev
            pre.next = node
        if node.next is not None:
            nex = node.next
            nex.prev = node

    def flag(self, flag):
        if flag == 'C':
            self.delete()
        elif flag == 'Z':
            self.ctrlz()
        else:
            f, s = flag.split(' ')
            if f == 'U':
                self.move(f, int(s))
            else: # D
                self.move(f, int(s))

    def ox(self, n):
        res = ['O'] * n
        for d in self.delq:
            res[d.data] = 'X'
        return "".join(res)

    def printall(self):
        tmp = self.head
        a = []
        b = []
        while tmp:
            a.append(tmp.data)
            tmp = tmp.next
        for d in self.delq:
            b.append(d.data)

        print(a, b, self.cur.data)

def solution(n, k, cmd):
    answer = ''

    linked_list = {i: [i - 1, i + 1] for i in range(1, n+1)} #n=8일때 1~8까지
    OX = ["O" for i in range(1,n+1)]
    stack = []

    k += 1

    for c in cmd:
        if c[0] == 'D':
            for _ in range(int(c[2:])):
                k = linked_list[k][1]
        elif c[0] == 'U':
            for _ in range(int(c[2:])):
                k = linked_list[k][0]
        elif c[0] == 'C':
            prev, next = linked_list[k]
            stack.append([prev, next, k])
            OX[k-1] = "X"

            if next == n+1:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]

            if prev == 0:
                linked_list[next][0] = prev
            elif next == n+1:
                linked_list[prev][1] = next
            else:
                linked_list[prev][1] = next
                linked_list[next][0] = prev

        elif c[0] == 'Z':
            prev, next, now = stack.pop()
            OX[now-1] = "O"

            if prev == 0:
                linked_list[next][0] = now
            elif next == n+1:
                linked_list[prev][1] = now
            else:
                linked_list[prev][1] = now
                linked_list[next][0] = now

    return "".join(OX)

'''