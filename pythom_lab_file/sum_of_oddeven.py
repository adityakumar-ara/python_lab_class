# list = [1,2,3,4,5,6,7,8]
# evensum = 0
# oddnsum = 0
# for i in list:
#     if i % 2:
#        evensum=+i
#     else:
#         oddnsum=+i 

# print(evensum)        
# print(oddnsum)  
    
list = []
evensum = 0
oddsum = 0
n = int(input("enter number"))
for i in range (1,n+1):
    m = int(input("enter elements"))
    list.append(m)    
print(list) 

for i in list:
    if i % 2==0:
        evensum+=i
    else:    
        oddsum+=i
print(evensum)        
print(oddsum)        