origin = {}
Owords = []
newwords = []
n,m = input().split(" ")
n = int(n)
m = int(m)
for i in range(n):
    key,value = input().split(" ")
    origin[key] = value
    Owords.append(key)
def judge(word):
    tmp = ''
    cnt = 0
    for Oword in Owords:
        if Oword in word:
            cnt+=1
            tmp += origin[Oword]
            start = word.find(Oword)
            word = word[:start]+word[start+len(Oword):]
            if cnt == 2:
                break
    if len(word)!=0:
        tmp = 'E'
    print(tmp)
for j in range(m):
    newword = input()
    judge(newword)
    newwords.append(newword)