n = int(input("Enter your number : "))
sum_even = 0
for i in range (2 , n + 1 , 2):
    sum_even += i
print(f"The sum of even numbers up to {n} is: {sum_even}")