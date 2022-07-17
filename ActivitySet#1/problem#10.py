# Dictionaries

# filename = "dataset/mbox-short.txt"
# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)
# names={}
# name=[]
# for line in handle:
#     if line.startswith('From '):
#         line=line.split()
#         name=line[1]
#     	if name not in names :
#         	names[name]=1
#     	else:
#         	names[name]=names[name]+1
            
# values=names.values()
# max_value=max(values)
# for key,value in names.items():
#     if max_value==value:
#        nm=key
# print(nm,max_value
print('=====================================')
dic_t={}
with open(input('enter the file :'),'r') as f:
    for line in f:
        if line.startswith('From '):
            email=line.split()
            dic_t[email[1]]=dic_t.get(email[1],0)+1
print(dict((b,a) for a,b in dic_t.items()).get(max(dic_t.values())),max(dic_t.values()))