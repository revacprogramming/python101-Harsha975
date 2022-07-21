n=int(input())
s={}
for i in range(n):
    m=int(input())
    if m==0:
        s[0]=1
        print('{} points : {} ways'.format(m,s[m])) 
        continue
    n1,n2,a=0,0,0
    n3=1
    for j in range(m):
        a=n1+n2+n3
        n1=n2
        n2=n3
        n3=a
        s[m]=a
    print('{} points : {} ways'.format(m,s[m])) 