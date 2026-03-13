import sys
n,m = map(int, sys.stdin.readline().split())

L = list(map(int, sys.stdin.readline().split()))


start = 0
end = max(L)
answer=0
while start<=end:
    middle = (start+end)//2
    total=0
    for l in L:
        if l-middle>0:
            total += (l-middle)
            if total>=m:
                break

    if total<m:
        end = middle-1
    else:
        answer = middle
        start = middle+1

print(answer)