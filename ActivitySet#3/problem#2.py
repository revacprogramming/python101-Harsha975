def ans(ls):
    lst2=[]
    sum=0
    for z in ls:
        f1=f(f(1,z))
        lst2.append(f1)
    for x in lst2:
        sum+=x  
    for h in range(len(lst2)-1):
        print(lst2[h],end='  +  ' )
    print(lst2[-1],' = ', sum) 
    return sum
def main():
    lst=[]
    n=int(input('input enter the no of sample :'))
    for i in range(n):
        m=int(input('enter the no of fraction u want :'))
        for j in range(m):
            den=int(input('enter the den:'))
            lst.append(den)
        result=ans(lst)
        lst.clear()
main()