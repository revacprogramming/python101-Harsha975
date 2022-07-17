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
fh.close()
'''02'''
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh :
    if line.startswith("From "):
            print(line.split()[1])
            count+=1
print("There were", count, "lines in the file with From as the first word")
fh.close()
