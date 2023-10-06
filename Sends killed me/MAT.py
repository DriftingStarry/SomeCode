def GetMat():
    R1,C1 = input().split(" ")
    R1,C1 = int(R1),int(C1)
    MAT = []
    for i in range(R1):
        tmp = list(map(int,input().split(" ")))
        MAT.append(tmp)
    return R1,C1,MAT
R1,C1,MAT1 = GetMat()
R2,C2,MAT2 = GetMat()
def printMat(MAT):
    for i in range(len(MAT)):
        print(*MAT[i],sep=' ')

def dotMATs(MAT1,MAT2):
    result = [[0 for j in range(len(MAT2[0]))] for i in range(len(MAT1))]
    for i in range(len(MAT1)):
        for j in range(len(MAT2[0])):
            for k in range(len(MAT2)):
                result[i][j] += MAT1[i][k]*MAT2[k][j] 
    return result

if C1!=R2:
    print("Error: "+str(C1)+" != "+str(R2))
else:
    print(R1,C2)
    MAT3 = dotMATs(MAT1,MAT2)
    printMat(MAT3)