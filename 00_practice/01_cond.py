# Write a program that takes an integer as input and determines if it is positive, negative, or zero. 

value_input = int(input("Input the Number"))

if value_input < 0:
    print("It is Negative number")
elif value_input > 0:
    print("It is +ve number")
elif value_input == 0:
     print("It is Zero")



# Write a program that calculates the sum of all numbers from 1 to 100.

total_sum = 0

for number in range(1,5):
    total_sum += number

print(total_sum)    