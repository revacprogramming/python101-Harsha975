# Tuples

filename = "dataset/mbox-short.txt"
result={}

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if line.startswith("From "):
    	time=line.split()[5]
        hour=time.split(":")[0]
        result[hour]=result.get(hour,0)+1
           
rr=()            
rr=sorted(result.items())
for a,b in rr:
    print(a,b)
