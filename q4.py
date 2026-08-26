
total_elements = int(input("How many numbers do you want to enter? "))

numbers = []


for i in range(total_elements):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)


total_sum = sum(numbers)

print("Sum of all elements:", total_sum)