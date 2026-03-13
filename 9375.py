import sys
from collections import defaultdict

def asdf():
    d = defaultdict(list)
    n = int(sys.stdin.readline())
    if n==0:
        print(0)
        return
    result = 1
    for _ in range(n):
        name, category = map(str, sys.stdin.readline().split())
        d[category].append(name)
    for x in d:
        result *= (d[x].__len__()+1)
    print(result-1)

t = int(sys.stdin.readline())

for _ in range(t):
    asdf()
