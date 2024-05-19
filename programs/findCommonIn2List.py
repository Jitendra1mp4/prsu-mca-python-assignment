# Python program to find common elements in two lists
import introJitendra
introJitendra.printIntro("program to find common elements in two lists.")

list1 = list()
list2 = list()

print("enter 5 values for list 1 ")
for i in range(5):
    list1.append(int(input()))
    

print("enter 5 values for list 2 ")
for i in range(5):
    list2.append(int(input()))
    
common_elements = list(set(list1) & set(list2))
print("Common elements:", common_elements)

