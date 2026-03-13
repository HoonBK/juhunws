n,m = map(int, input().split())
L= list()
for _ in range(n):
    a = int(input())
    L.append(a)

L.sort()
max = max(L)

min=1
result=0
while min<=max:
    middle = (min+max)//2
    count = sum(l // middle for l in L)

    if count>=m:
        result=middle
        min = middle+1
    elif count<m:
        max = middle-1


print(result)
    


