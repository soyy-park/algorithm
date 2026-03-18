import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
import heapq

N = int(input())
heap = []

for _ in range(N):
    x = int(input())    # 자연수: x를 추가 / 0: 가장 작은 값 출력 및 제거
    if x:
        heapq.heappush(heap, x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)