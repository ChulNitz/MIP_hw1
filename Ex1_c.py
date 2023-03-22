import random


# Receive user input
input_nums = []
for i in range(3):
    num = input(f"Enter integer {i+1} between 0 and 9: ")
    while not num.isdigit() or int(num) < 0 or int(num) > 9:
        num = input(f"Invalid input! Enter integer {i+1} between 0 and 9: ")
    input_nums.append(int(num))


print("user input numbers:", input_nums)

# Generate random numbers
random_nums = [random.randint(0, 9) for i in range(3)]

print("random numbers:", random_nums)

# Check for matches regardless of order
input_nums.sort()
random_nums.sort()

if input_nums == random_nums:
    print("I WIN")
else:
    print("I LOSE")

