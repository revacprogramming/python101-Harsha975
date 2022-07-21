n=int(input())
for q in range(n):
    len=int(input('\n'))
    s=list(map(int,input().split()))
    x=0
    lst=[]
    for i in range(0,len):
        if (x>=len):
            break
        else:
            if s[x]==0 and s[x+1]!=0:
                a=str(s[x+2])*s[x+1]
                lst.append(a.split())
                for e in lst:
                    for g in e:
                        for h in g:
                            print(h,end=' ')
                x=x+3
                lst.clear()
            elif s[x]==0 and s[x+1]==0:
                print(s[x],end=' ')
                x=x+2
            else:
                print(s[x],end=' ')
                x+=1