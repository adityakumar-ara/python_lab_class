string = input("enter any string")

print("Enter 1. for find frequncy of character in string")
print("Enter 2. replace charater another charector")
print("Enter 3. remove first of character in string")
print("Enter 4. remove all charater in string")
a = int (input("Choose an option:"))
if a == 1:
   s = input("enter count word in string")
   print(string.count(s))
elif a==2:
   s = input("enter word who want to replace")
   m = input("enter new word")
   print(string.replace(s,m))   
elif a == 3:
