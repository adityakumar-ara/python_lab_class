a = input()

a = a.casefold()
a1 = reversed(a)

if list(a) == list(a1):
    print("Number Palindrom")
else:
    print("Not a Palindrom")