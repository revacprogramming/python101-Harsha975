# Files

#filename = "dataset/mbox-short.txt"

count=0
total=0
fname = input("Enter file name: ")
fh = open(fname,'r')
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): 
        continue
    count=count+1
    index=line.find("0.")
    float_no=float(line[index:])
    total+=float_no
print("Average spam confidence:",total/count)
