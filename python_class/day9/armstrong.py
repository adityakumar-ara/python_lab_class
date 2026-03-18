num = int(input("Ek number enter karein: "))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum:
    print(f"{num} ek Armstrong number hai!")
else:
    print(f"{num} Armstrong number nahi hai.")