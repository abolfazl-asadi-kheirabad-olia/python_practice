#Function definition
def print_multiplication_table(numbers):
    for i in range(1, 11):
        row = ""
        for number in numbers:
            row += f"{number} × {i} = {number * i}\t"  # \t for spacing between columns
        print(row)

# Get input from the user
user_input = input("Please enter numbers (separated by spaces): ")
numbers = list(map(int, user_input.split()))  # Convert input to a list of numbers
# Use the function
print_multiplication_table(numbers)

