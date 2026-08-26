
total_elements = int(input("How many numbers do you want in the list? "))

numbers = []
for i in range(total_elements):
    num = float(input("Enter number " + str(i + 1) + ": "))
    numbers.append(num)

largest_number = max(numbers)

print("The largest number is:", largest_number)