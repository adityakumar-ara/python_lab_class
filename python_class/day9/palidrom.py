num = input("enter number")
num = num.casefold()
a = reversed(num)
if list(num) ==list(a):
    print("hello")
else:
    print("bye")    