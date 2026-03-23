def palidrom(num):
    num = num.casefold()
    
    reverse_num = reversed(num)
    
    if list(num) == list(reverse_num):
        print("hello")
    else:
        print("bye")      

user_input = input("Enter a word or number: ") 
              
palidrom(user_input)