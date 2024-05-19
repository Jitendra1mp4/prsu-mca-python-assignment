# Python program that takes a list of words from the user and writes them into a file
import introJitendra
introJitendra.printIntro("Write a Python program that takes a list of words from the user and writes them into a file. The program should stop when the user enters the word ‘quit’.")

words = []
while True:
    word = input("Enter a word (or type 'quit' to stop): ")
    if word == 'quit':
        break
    words.append(word)

with open("words.txt", "w") as file:
    for word in words:
        file.write(word + "\n")

print("Words have been written to 'words.txt'.")

