n=int(input())

size = [0,1,2]

for i in range(3,n+1):
    size.append(size[i-1]+size[i-2])

print(size[n]%10007)