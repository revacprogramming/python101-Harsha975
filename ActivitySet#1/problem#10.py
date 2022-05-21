# Dictionaries

# filename = "dataset/mbox-short.txt"
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
names={}
name=[]
for line in handle:
    if line.startswith('From '):
        line=line.split()
        name=line[1]
    	if name not in names :
        	names[name]=1
    	else:
        	names[name]=names[name]+1
            
values=names.values()
max_value=max(values)
for key,value in names.items():
    if max_value==value:
       nm=key
print(nm,max_value)