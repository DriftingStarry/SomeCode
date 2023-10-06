n,k = input().split(" ")
n = int(n)
k = int(k)
stus = {}
stusls = []
def cul(write,face):
    result = round(write/5 + face + 0.001,2)
    return result

def sort_down(lis):
    for i in range(len(lis)):
        for j in range(i,len(lis)):
            totali,totalj = stus[lis[i]][2],stus[lis[j]][2]
            facei,facej = stus[lis[i]][1],stus[lis[j]][1]
            numi,numj = stusls[i],stusls[j]
            if totali<totalj or totali == totalj and facei < facej or totali == totalj and facei == facej and numi > numj:
                lis[i],lis[j] = lis[j],lis[i]
for i in range(n):
    num,write,face = input().split()
    num,write,face = int(num),float(write),float(face)
    if write >= 500*0.6 and face >= 60:
        stus[num] = [write,face,cul(write,face)]
        stusls.append(num)      
sort_down(stusls)
get = stusls[:k]
print(*get,sep=' ')
linet = stus[get[-1]][-1]
linef = stus[get[-1]][-2]
print(linet,linef)

    