def r(sb):
    if (len(sb)>=3):
        return sb[::]==sb[::-1]
def main():
    n= int(input())
    for x in range(n):
        len=int(input())
        s=input()
        i=0
        j=0
        for i in range(len-2):
            for j in range(0,len):
                if(r(s[i:j+i+3])):
                    if j+i+3>len:
                        break
                    print(i+1,s[i:j+3+i])
main()