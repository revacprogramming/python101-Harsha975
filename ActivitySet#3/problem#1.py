# def rarea(f):
#   a=f[0]*(f[3]-f[5])
#   b=f[2]*(f[5]-f[1])
#   c=f[4]*(f[1]-f[3])
#   return(abs(a+b+c))


# def outpp(ch,resl):
#     j=0
#     for i in ch:
#         print(f'Area of rectangle with vertices ({ch[j][0]},{ch[j][1]}),({ch[j][2]},{ch[j][3]}),({ch[j][4]},{ch[j][5]}) is {resl[j]}')
#         j+=1
    
# ll,ch=[],[]
# for i in range(int(input())):
#   rl=list(map(float,input().split()))
#   ch.append(rl)
#   ll.append(rarea(rl))
  
# outpp(ch,ll)
def area(x1,x2,x3,y1,y2,y3):
    area=x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)
    return abs(area)
    
def main():
    areas=[]
    sides=[]
    n=int(input('enter the number of trinagle u want:'))
    for i in range(0,n):
        x1,y1,x2,y2,x3,y3=map(float,input('enter the coordinate(x1,y1) ,(x2,y2) ,(x3,y3) of the rectangle:').split())
        area_=area(x1,x2,x3,y1,y2,y3)
        sides.append((x1,y1,x2,y2,x3,y3))
        areas.append(area_)
    print(sides)
    j=0  
    for j in range(0,n):   
        print('''Area of rectangle with vertices ({},{}) ({},{}) ({},{}) is {}'.format(sides[j][0],sides[j][1],sides[j][2],sides[j][3],sides[j][4],sides[j][5],areas[j])''')   
main()