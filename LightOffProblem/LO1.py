# -*- coding: gbk -*-
import random 
'''
���Ǳ��ϵ�������������һ�д��������
def spawn(x,y):
    lis = []
    for i in range(y):
        lis.append([0]*x)
        for j in range(x):
            lis[i][j] = random.randint(0,1)
    return lis
'''
#��������lis
x = int(input("x"))
y = int(input("y"))
lis = [[random.randint(0,1) for i in range(x)] for j in range(y)]
lisT = [[0 for i in range(x)] for j in range(y)]
print("Ŀ��",lisT)
print("����",lis)
#��ӡ����lis
def Prlis(lis):
    for i in range(len(lis)):
        tmp=''
        for j in range(len(lis[i])):
            tmp+=str(lis[i][j])
        print(tmp)
#�ı�״̬
def change(x,y,lis):
    lis[x][y] = 1 - lis[x][y]
    if x == 0:
       lis[x+1][y] = 1 - lis[x+1][y]
    
        
        
#���������ȷ��
def check(x1,y1,x,y):
    if x1 >= x or y1 >= y:
        return False
    else:
        return True
#������
while True:
    print("���ڵ�����Ϊ��")
    Prlis(lis)
    tmp = input("���루������,����������114514��������")
    if tmp == "114514":
        print("ǿ�ƽ���")
        break
    elif lis == lisT:
        print("�ɹ�")
        break
    else:
        tmp = tmp.split(",")
        x1 = int(tmp[0])
        y1 = int(tmp[1])
        if check(x1,y1,x,y):
            change(x1,y1,lis)
        else:
            print("����������������")

        



     