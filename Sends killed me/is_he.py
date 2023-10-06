def is_he(n):
    flag = False
    if n <=2 :
      return flag
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            flag=True
    return flag
a = int(input())
ls = []
for i in range(4,a+1):
    if is_he(i):
        ls.append(i)
print(*ls,sep=' ')