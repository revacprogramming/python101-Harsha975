# Lists
'''01'''
filename = "dataset/romeo.txt"
fname = input("Enter file name: ")
fh = open(fname,'r')
lst=[]
for line in fh:
    for word in line.split():
        if word not in lst :
        	lst.append(word)
