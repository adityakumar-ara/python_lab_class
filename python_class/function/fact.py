def fact(n):
    if n ==1 or n < 1:
        return 1
    else:
        return n*fact(n-1)
    
n = int(input("enter any number"))
result = fact(n)  
print(result)      