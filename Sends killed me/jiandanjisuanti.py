NP = input()
npls = NP.split()
N = npls[0]
P = npls[1]
cnt = 0
for s in N:
    if P == s:
        cnt+=1
print(cnt)