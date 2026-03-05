# n = 5
# for i in range(5,0):
#     for j in range(i,0):
#         print(j , end="")
#     print() 

# name = input("enter name")
# # for text in name[0:3]:
# #     print(text)
# # for text in name[3:]:
# #     print(text)    

# for text in name[-1:-7:-1]:
#     print(text)

n = int (input("enter number"))
for i in range(1,n):
    if i%5==0:
        continue
    print(i)   