# for i in range(0,10):
#     print(i)
#     if(i==4):
#         break

# for i in range(0,11):
#     print(i)
# else:
#     print("done")    

# list = {1,2,3,4,5}
# for item in list:
#     print(item)
# else:
#     print("list element print done")    


lst = [1,2,3,4,5,6,7,8,9]
n = int(input("Enter number to search: "))

for index in range(len(lst)):
    if lst[index] == n:
        print("Your number is found at index", index)
        break
else:
    print("Number not found")
