# Functions
def computepay(h, r):
    if h <=40 :
    	p=h*r
    else :
    	p=(40*r) + ((h-40)*r*1.5)
    return p

hrs = input("Enter Hours:")
hrs=float(hrs)
rte= input("enter the rate:")
rte=float(rte)
p = computepay(hrs, rte)
print("Pay", p)