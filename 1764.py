import sys

n,m = map(int, sys.stdin.readline().split())
d = dict()
answer=list()

for i in range(n):
    name = sys.stdin.readline().strip()
    d[name] = 'N'

for i in range(m):
    name = sys.stdin.readline().strip()
    if name in d:
        answer.append(name)

answer.sort()
print(answer.__len__())
for a in answer:
    print(a)