import sys

n,m = map(int, sys.stdin.readline().split())

d=dict()
l=list()
l.append('zero')

for i in range(1,n+1):
    name = str(sys.stdin.readline().strip())
    d[name]=i
    l.append(name)

for i in range(1,m+1):
    input = str(sys.stdin.readline().strip())
    if input.isdigit()==True:
        input = int(input)
        print(l[input])
    else:
        print(d[input])