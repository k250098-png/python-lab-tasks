
total_elements = int(input("How many numbers do you want to enter? "))

numbers = []
even_count = 0

for i in range(total_elements):
    num = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(num)

    if num % 2 == 0:
        even_count += 1

print("Count of even numbers:", even_count)