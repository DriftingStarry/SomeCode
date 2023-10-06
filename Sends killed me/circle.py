m,n = input().split(' ')
m = int(m)
n = int(n)
maxx = maxy = m
minx = miny = n
for i in range(m,n):
    for j in range(m,n):
        if abs(i*i-i*j-j*j) == 1:
            if i>maxx and j >maxy:
                maxx,maxy = i,j
            if i<minx and j < miny:
                minx,miny = i,j
print("("+str(maxx)+","+str(maxy)+")")
print("("+str(minx)+","+str(miny)+")")