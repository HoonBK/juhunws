import heapq
import sys
input = sys.stdin.readline

heap = []

n = int(input())
for _ in range(n):
    a = int(input())
    if a>0:
        a = -a
        heapq.heappush(heap, a)
    elif a==0 and len(heap)==0:
        print(0)
    else:
        b = -heapq.heappop(heap)
        print(b)

