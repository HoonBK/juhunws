import sys

n,m = map(int, sys.stdin.readline().split())
l = list()
l.append(0)
sum=0

num = list(map(int, input().split()))
for temp in num:
    sum +=temp
    l.append(sum)

for _ in range(m):
    i,j = map(int, sys.stdin.readline().split())
    print(l[j] - l[i-1])