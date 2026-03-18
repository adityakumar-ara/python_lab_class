# num = input("enter number")
# num = num.casefold()
# a = reversed(num)
# if list(num) ==list(a):
#     print("hello")
# else:
#     print("bye")    

num = input("enter number")

if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")