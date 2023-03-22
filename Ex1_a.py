numbers = []
while True:
    num = input("Enter a number or 'a' to exit: ")
    if num == 'a':
        break
    else:
        numbers.append(float(num))

if numbers:
    average = sum(numbers) / len(numbers)
    print(f"The average of the entered numbers is: {average}")
else:
    print("No numbers were entered.")
