import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
# L = deque(map(int, input().split()))
L = list(map(int, input().split()))
k = int(input())

x = N//k

answer=[]

# for i in range(N//x):
#     temp=[]
#     for _ in range(x):
#         temp.append(L.popleft())
#     temp.sort()
#     for t in temp:
#         answer.append(t)

for i in range(0,N,x):
    temp = L[i:i+x]
    temp.sort()
    answer.extend(temp)


print(*answer)