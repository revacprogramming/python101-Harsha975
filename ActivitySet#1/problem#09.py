# Lists

filename = "dataset/romeo.txt"
fname = input("Enter file name: ")
fh = open(fname,'r')
lst=[]
for line in fh:
    for word in line.split():
        if word not in lst :
        	lst.append(word)
print(sorted(lst))
# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "mbox-short.txt"

# fh = open(fname)
# count = 0

# for line in fh :
#     if line.startswith("From"):
#     	count+=1
#         print(line)

# print("There were", count, "lines in the file with From as the first word")