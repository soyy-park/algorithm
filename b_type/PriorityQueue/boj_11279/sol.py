import sys
sys.stdin = open('input.txt')


import sys
import heapq
input = sys.stdin.readline
N = int(input())
lst = []

for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(lst, -x)
    else:
        if lst:
            print((-1) * (heapq.heappop(lst)))
        else:
            print(0)