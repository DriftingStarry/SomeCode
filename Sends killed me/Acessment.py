import time
startt = time.time()
n,k = input().split(" ")
n = int(n)
k = int(k)
stus = []
for i in range(n):
    stus.append(list(map(float,input().split(" "))))
def cul(stu):
    result = round(stu[1]/5 + stu[2]+0.01,2)
    return result
for i in range(len(stus)):
    stu = stus[i]
    stus[i].append(cul(stu))
def sort_down(lis):
    for i in range(len(lis)):
        swarped = False
        for j in range(i,len(lis)):
            if lis[i][3] < lis[j][3] or lis[i][3] == lis[j][3] and lis[i][2] < lis[j][2] or lis[i][3] == lis[j][3] and lis[i][2] == lis[j][2] and lis[i][0] > lis[j][0]:
                lis[i],lis[j] = lis[j],lis[i]
                swarped = True
        if not swarped:
            break
sort_down(stus)
get = []
for i in range(k):
    get.append(int(stus[i][0]))
print(*get,sep=' ')
print(str(stus[i][3])+' '+str(stus[i][2]))
endt = time.time()
print(endt-startt)