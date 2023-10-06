day = int(input())
walk = input().split(' ')
walks = list(map(int,walk))
walks.sort(reverse=True)
for i in range(day,0,-1):
    cnt=0
    for j in walks:
        if j>i:
            cnt+=1
        else:
            break
    if cnt>=i:
        break
print(i)