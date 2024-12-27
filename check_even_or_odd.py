#Function definition
def is_even(a):
    if a % 2 == 0:
        return "The number is even"
    else:
        return "The number is not even"

#Getting input from the user    
a = int(input("Enter your number: "))

#Function call
even = is_even(a)

#Print result
print(even)