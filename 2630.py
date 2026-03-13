import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

def asdf(arr, x,y,n):
    color = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j]!=arr[x][y]:
                half = n//2
                w1,b1 = asdf(arr,x,y,half)
                w2,b2 = asdf(arr,x,y+half,half)
                w3,b3 = asdf(arr,x+half,y,half)
                w4,b4 = asdf(arr,x+half,y+half,half)
                return (w1+w2+w3+w4, b1+b2+b3+b4) 

    if color ==0:
        return (1,0)
    else:
        return (0,1)

w, b = asdf(arr,0,0,n)
print(w)
print(b)