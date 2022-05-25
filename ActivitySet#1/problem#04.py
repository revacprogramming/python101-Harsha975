# Conditional Execution

'''01 QUESTION

hrs = input("Enter Hours:")
h = float(hrs)
rate=input("enter the rate :")
r=float(rate)
if h<=40:
  gross=h*r
else:
  gross=(40*r)+((h-40)*(r*1.5))
print(gross)  
 
score = float(input("Enter Score: "))
if score > 1.0:
    
	  print('error')
    
elif score >=0.9 :
    print ('A')

elif score >=0.8 :
    print ('B')
    
elif score >=0.7 :
    print ('C')
    
elif score >=0.6 :
    print ('D')
  
elif score <0.6 :
    print ('F')