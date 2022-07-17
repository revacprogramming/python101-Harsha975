# Files

#filename = "dataset/mbox-short.txt"

# count=0
# total=0
# fname = input("Enter file name: ")
# fh = open(fname,'r')
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"): 
#         continue
#     count=count+1
#     index=line.find("0.")
#     float_no=float(line[index:])
#     total+=float_no
# print("Average spam confidence:",total/count)
count=0
total=0
with open(input('enter the file '), 'r') as f:
    for line in f:
        if line.startswith('X-DSPAM-Confidence:'):
            total+=float(line[line.find('0.'):])
            count+=1           
print('Average spam confidence:',total/count)
