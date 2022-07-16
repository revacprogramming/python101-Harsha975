# Files

#filename = "dataset/mbox-short.txt"

count=0
total=0
with open(input('enter the file '), 'r') as f:
    for line in f:
        if line.startswith('X-DSPAM-Confidence:'):
            total+=float(line[line.find('0.'):])
            count+=1           
print('Average spam confidence:',total/count)
