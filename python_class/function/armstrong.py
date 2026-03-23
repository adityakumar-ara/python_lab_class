def armstong(num):
    if num <=0:
        return False
    temp = num
    sum = 0
    order = len(str(num))
    while(temp > 0):
        rim = temp % 10
        sum = sum+(rim**order)
        temp //= 10
    if num == sum:
        return True    
    else:
       return False

num = int(input("enter any number"))        
if armstong(num):
    print("hello")
else :
    print("bye")    