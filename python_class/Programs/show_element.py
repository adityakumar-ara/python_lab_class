def show_elements(lst, tup, dic):
    print("List elements:")
    for item in lst:
        print(item)

    print("\nTuple elements:")
    for item in tup:
        print(item)

    print("\nDictionary elements:")
    for key in dic:
        print(key, ":", dic[key])
    
#    # if find all key and values
#     print("\nDictionary elements:")
#     for key,values in dic.items():
#         print(key, ":", values)

# Data
my_list = [10, 20, 30]
my_tuple = (1, 2, 3)
my_dict = {"name": "Aditya", "age": 20, "course": "BCA"}

# Function call
show_elements(my_list, my_tuple, my_dict)