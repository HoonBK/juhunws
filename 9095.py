a = int(input())

list = [0,1,2,4]
for x in range(10):
    list.append(list[x+1]+list[x+2]+list[x+3])

for i in range(a):
    b = int(input())
    print(list[b])