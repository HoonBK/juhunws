l = [0,1,1,1,2,2]

for i in range(6,102):
    l.append(l[i-1] + l[i-5])


t = int(input())

for i in range(t):
    n = int(input())
    print(l[n])