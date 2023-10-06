N = int(input())
islands = [[] for j in range(N+1)]
k,w = input().split(' ')
k = int(k)
w = int(w)
for i in range(k):
    a,b = input().split(' ')
    a = int(a)
    b = int(b)
    islands[a].append(b)
    islands[b].append(a)
print(islands)
    
def judge(start,end):
    flag = False
    q = ['']*1000
    visited=[]
    head = tail = 0
    q[tail] = start
    tail += 1
    visited.append(start)
    while head < tail and not flag:
        for i in islands[q[head]]:
            print(i)
            if i not in visited:
                q[tail] = i
                tail += 1
                visited.append(i)
            if i == end:
                flag = True
        head += 1
        print(head,tail)
    return flag
for i in range(w):
    ss = input().split(' ')
    start = int(ss[0])
    end = int(ss[1])
    if judge(start,end):
        print("NO")
    else:
        print("YES")