# Files

#filename = "dataset/mbox-short.txt"

c=0.0
count=0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
 
     count+=1
     a=line.find(':')
     b=line[a+2:]
     b=float(b)
     c+=b
d=c/count
print("Average spam confidence: ",d)
