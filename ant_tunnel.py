# 백준 #14725 개미굴
'''
    Algorithm: Trie Algorithm, dfs
    Time Complexity: O(NKt)

    N => leaf node의 개수
    트라이 알고리즘을 써 보자.
'''
import sys
from typing import List, Tuple, Callable

FLOOR = '--'

class Node:
    def __init__(self, value:str, flag:bool=False):
        self.value = value
        self.flag = flag
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string:List[str]):
        cur_node = self.head

        for s in string:
            if s not in cur_node.child:
                cur_node.child[s] = Node(s)
            cur_node = cur_node.child[s]
        # 마지막 문자에 flag
        cur_node.flag = True

    def search(self, string:List[str]):
        cur_node = self.head

        for s in string:
            if s in cur_node.child:
                cur_node = cur_node.child[s]
            else:
                return False

        if cur_node.flag:
            return True
        else:
            return False

    def get_tunnel(self) -> str:
        ''' 개미굴 반환 '''
        res = []
        stack = []

        for c in self.head.child:
            stack.append((0, self.head.child[c]))

        while stack:
            lev, cur_node = stack.pop()

            res.append(FLOOR*lev + cur_node.value)

            for c in cur_node.child:
                stack.append((lev+1, cur_node.child[c]))

        return "\n".join(res)


def input() -> Callable:
    return sys.stdin.readline().rstrip()


def read_data() -> Tuple:
    N = int(input())
    info = [input().split()[1:] for _ in range(N)]
    return N, info


def solution(N: int, info: List[List[str]]) -> str:
    ant_tunnel = Trie()

    # 사전순으로 앞서는 문자를 dfs를 사용해 뽑기 위해 역순 정렬
    for route in sorted(info, reverse=True):
        ant_tunnel.insert(route)

    return ant_tunnel.get_tunnel()


if __name__ == "__main__":
    print(solution(*read_data()))

