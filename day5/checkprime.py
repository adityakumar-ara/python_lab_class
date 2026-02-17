# n = int (input("enter your number:"))
def checkprime(n):
 count = 0
 for i in range(1,n+1):
   if (n%i==0):
    count+=1
 if(count==2):
   print("this is prime number:")   
 else:
   print("not prime") 
checkprime(6) 
   

# checkprime(5)   