# Calculate average marks, percentage and grade of a student:
import introJitendra

introJitendra.printIntro("Calculate average marks, percentage and grade of a student:")

n = 5
total = 0
for i in range(n):
    m = int(input(f"Enter marks for subject {i+1}: "))
    total += m
average = total / n
percentage = (total / (n * 100)) * 100
print("Average Marks: ", average)
print("Percentage: ", percentage)

# Grade
print("Grade : ", end="")
if percentage >= 90 : print("A+") 
elif percentage >= 80 : print("A")
elif percentage >= 70 : print("B+")
elif percentage >= 60 : print("B") 
elif percentage >= 50 : print("C")
else : print("D")
