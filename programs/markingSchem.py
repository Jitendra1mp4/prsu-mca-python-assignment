#  program to get marks in five subjects from user calculate average marks, percentage and grade of a student
import introJitendra

introJitendra.printIntro(
    "program to get marks in five subjects from user calculate average marks, percentage and grade of a student"
)

# Python Program to Calculate Total Marks Percentage and Grade of a Student

print("Enter the marks of subjects:")
total = 0 
for i in range(5):
    print("enter marks for subject ", (i+1), end=" : ")
    total += float(input())

# Calculate the Total, Average, and Percentage
average = total / 5.0
percentage = (total / 500.0) * 100

# Determine the grade based on the average
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B+"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C+"
elif percentage >= 40:
    grade = "C"
elif percentage >= 33:
    grade = "D"
else:
    grade = "E"

# Display the results
print("\nThe Total marks is:\t", total, "/ 500.00")
print("The Average marks is:\t", average)
print("The Percentage is:\t", percentage, "%")
print("The Grade is:\t\t", grade)
