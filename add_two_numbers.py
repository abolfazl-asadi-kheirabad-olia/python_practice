def add_numbers():
    while True:
        try:
            # Asking the user for two numbers
            a = int(input("Enter your number 1: "))
            b = int(input("Enter your number 2: "))
            result = a + b  # Calculate the sum of the two numbers
            return result 
        except ValueError:
            # If the user enters an invalid number, ask again
            print("Please enter a valid number.")

while True:
    # Call the function to get the sum of the two numbers
    total = add_numbers()
    print(f"The sum of the two numbers is: {total}")
    
    # Ask the user if they want to continue
    continue_prompt = input("Do you want to continue? (yes/no): ").strip().lower()
    if continue_prompt != "yes":
        # If the user doesn't want to continue, exit the loop
        print("Goodbye!")
        break
