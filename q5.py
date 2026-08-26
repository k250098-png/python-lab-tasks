
total_elements = int(input("How many numbers do you want in the list? "))

numbers = []
for i in range(total_elements):
    num = float(input("Enter number " + str(i + 1) + ": "))
    numbers.append(num)

threshold = float(input("Enter the target number: "))

filtered_list = []
for num in numbers:
    if num >= threshold:
        filtered_list.append(num)

print("Updated list:", filtered_list)
