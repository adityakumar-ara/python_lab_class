# for i in range(0,50):
#     if i %5 != 0:
#         print(i)
# n = 1
# num = 50
# while(n<=num):
#     if n %5 != 0:
#         print(n)
#     n+=1

n = 1
num = 50
while(n<=num):
    if n %5 == 0:
        n+=1
        continue

    else:
        print(n)
        n+=1
    