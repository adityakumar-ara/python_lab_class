# Python mein split() method ke alag-alag examples

print("--- 1. Default Split (Spaces ke hisaab se) ---")
sentence = "Python sikhna sach mein mazedar hai"
words_list = sentence.split()
print(f"Original String: '{sentence}'")
print(f"Split List: {words_list}\n")


print("--- 2. Custom Separator (Comma ke hisaab se) ---")
csv_data = "apple,banana,mango,orange"
fruits_list = csv_data.split(",")
print(f"Original String: '{csv_data}'")
print(f"Split List: {fruits_list}\n")


print("--- 3. Maxsplit ka istemal (Limit lagana) ---")
log_info = "Error:Network:Timeout:120s"
# Sirf pehle 2 colon (:) par split karenge, baaki waise hi rahega
limited_list = log_info.split(":", 2)
print(f"Original String: '{log_info}'")
print(f"Split List: {limited_list}\n")


print("--- 4. Practical Use: User se input lena ---")
# User se ek line mein multiple values lene ke liye split() bahut kaam aata hai
user_input = input("Apne 3 doston ke naam space dekar likhiye: ")
friends = user_input.split()
print(f"Aapke doston ki list: {friends}")