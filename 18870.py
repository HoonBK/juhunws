import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int,input().split()))
S = set(L)
S = sorted(S)
D = dict()

for i in range(len(S)):
    D[S[i]] = i

answer = []

for l  in L:
    answer.append(D[l])

print(* answer)
