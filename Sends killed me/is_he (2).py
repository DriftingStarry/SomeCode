def is_he(n):
    flag = False
    if n <= 2:
        return flag
    elif n%2 == 0:
        flag=True
    else:
        i=3
        while i*i <= n:
            if n%i == 0:
                flag=True
            i+=2
    return flag
a = int(input())
ls = []
for i in range(a+1):
    if is_he(i):
        ls.append(i)
print(*ls,sep=' ')