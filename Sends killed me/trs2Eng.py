ss = input("N")
ls = ["zero","one","two","three","four","five","six","seven","eight","nine"]
flag = False
if len(ss) == 2 and ss[0] == ss[1]:
    flag = True
for s in ss[:-1]:
    tmp = int(s)
    tmp = ls[tmp]
    if flag:
        print("double",tmp)
        break
    else:
        print(tmp+" ",end="")
if not flag:
    tmp = int(ss[-1])
    tmp = ls[tmp]
    print(tmp)