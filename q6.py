
physics = float(input("Enter marks for Physics: "))
chemistry = float(input("Enter marks for Chemistry: "))
maths = float(input("Enter marks for Maths: "))


marks_dict = {
    "Physics": physics,
    "Chemistry": chemistry,
    "Maths": maths
}


total_marks = sum(marks_dict.values())
average_marks = total_marks / len(marks_dict)


highest_subject = max(marks_dict, key=marks_dict.get)

# Step 5: Display results
print(f"Average Marks: {average_marks:.2f}")
print(f"Subject with Highest Marks: {highest_subject}")