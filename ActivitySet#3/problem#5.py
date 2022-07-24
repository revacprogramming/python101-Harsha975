still yet to do.
s=[list(map(int,input().split())) ,
list(map(int,input().split())) ,
list(map(int,input().split())),
list(map(int,input().split())) ,
list(map(int,input().split())) ,
list(map(int,input().split())),
list(map(int,input().split())),
list(map(int,input().split())),
list(map(int,input().split()))]
# print(np.matrix(s))

def possible(row,column,number):
    #is the no is in row
    global s
    for i in range(0,9):
        if s[row][i]==number:
            # print(s[row][i])
            return False
    #is the no is in column
    for i in range(0,9):
        if s[i][column]==number:
            # print(s[column][i])
            return False

    #is the no is in square
    x0=(column//3)*3
    y0=(row//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if s[y0+i][x0+j]==number:
                return False
    return True
def solve():
    global s
    for row in range(0,9):
        for column in range(0,9):
            if s[row][column]==0:
                for number in range(1,10):
                    if possible(row,column,number):
                        s[row][column]=number
                        solve()
                        s[row][column]=0
                print('dont have ans')
                return
    
    print(np.matrix(s))

solve()