import sys
input = sys.stdin.readline
N, r, c = map(int, input().split())

size = 2**N

def asdf(size, r,c):
    count =0
    
    if size==1:
        return 0
    
    half = size//2

    if r<half and c<half: #1사분면
        count+=asdf(half, r,c)
    elif r<half and c>=half: #2사분면
        count+= (half)**2 + asdf(half, r,c-(half))
    elif r>=half and c<half: #3사분면
        count+= ((half)**2)*2 + asdf(half, r-(half), c)
    else: #4사분면
        count+= ((half)**2)*3 + asdf(half, r-(half), c-(half))

    
    return count

print(asdf(size,r,c))