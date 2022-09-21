### 2 ###
from itertools import combinations
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]

for comb in list(combinations(nums, M)):
    print(" ".join(list(map(str, comb))))

### 4 ###
from itertools import combinations_with_replacement
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]

for perm in list(combinations_with_replacement(nums, M)):
    print(" ".join(list(map(str, perm))))

### 5 ###
from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = map(int, input().split())

for perm in sorted(permutations(nums, M)):
    print(" ".join(list(map(str, perm))))

### 8 ###
import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))

for comb in combinations_with_replacement(nums, M):
    print(" ".join(list(map(str, comb))))