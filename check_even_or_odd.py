def is_even(a):
    if a % 2 == 0:
        return "The number is even"
    else:
        return "The number is not even"
    
a = int(input("Enter your number: "))

even = is_even(a)
print(even)