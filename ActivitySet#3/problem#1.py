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