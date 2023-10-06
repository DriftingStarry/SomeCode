N = int(input())
dic = {"Rock":"Paper","Paper":"Scissors","Scissors":"Rock"}
cnt = 0
while True:
    inc = input()
    if inc == "End":
        break
    elif cnt<N :
        out = dic[inc]
        print(out)
        cnt+=1
    else:
        cnt=0
        print(inc)