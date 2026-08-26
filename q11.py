
marks_dict = {}

for i in range(3):
    subject = input("Enter subject " + str(i + 1) + " name: ")
    marks = float(input("Enter marks for " + subject + " (out of 100): "))
    marks_dict[subject] = marks


total_marks = sum(marks_dict.values())

average = total_marks / len(marks_dict)


percentage = (total_marks / 300) * 100


print("Marks Dictionary:", marks_dict)
print("Average Marks:", average)
print("Percentage:", percentage, "%")