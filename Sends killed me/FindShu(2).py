d = day = int(input('N'))
walks = input('walk').split(' ')
walks = list(map(int,walks))
def sort_down(lis):
    for i in range(len(lis)):
        for j in range(i,len(lis)):
            if lis[i]<lis[j]:
                lis[i],lis[j] = lis[j],lis[i]
    return lis
walks_sort = sort_down(walks)
total = 1
while total <= d:
    total = 1
    for i in walks:
        if d < i:
            total+=1
    d -= 1
print(d)