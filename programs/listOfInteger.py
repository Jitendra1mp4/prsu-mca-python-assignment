#Python function to take a list of integers as input and return the averageimport introJitendra
import introJitendra
introJitendra.printIntro("Python function to take a list of integers as input and return the average")
def calculate_average(numbers):
    total = 0
    for i in numbers:
        total += i
    return total / len(numbers)

num_list = list()
for i in range(5):
    num_list.append(int(input("enter number : ")))
print("list is : ", num_list)
avg = calculate_average(num_list)
print(f"The average of the list is: {avg}")
