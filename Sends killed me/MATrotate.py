global N
N = int(input())
def GetMat():
    MAT = []
    for i in range(N):
        tmp = input().split(" ")
        MAT.append(tmp)
    return MAT
def RotateOutput(MAT):
    for i in range(N):
        ls = []
        for j in range(-1,-N-1,-1):
            ls.append(MAT[j][i])
        print(*ls,sep=' ')    
MAT = GetMat()
RotateOutput(MAT)