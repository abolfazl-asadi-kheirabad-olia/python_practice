#Function definition
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Using the function
num = 5
print(f"Factorial {num} is equal to {factorial(num)}")
