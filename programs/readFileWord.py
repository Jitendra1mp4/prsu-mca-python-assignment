# Python program that reads a file in text mode and counts the number of words that contain any one of the letters ['w', 'o', 'r', 'd', 's']
import introJitendra
introJitendra.printIntro("reads a file in text mode and \ncounts the number of words that\ncontain any one of the letters ['w', 'o', 'r', 'd', 's'].")

letters = set(['w', 'o', 'r', 'd', 's'])
word_count = 0

with open("words.txt", "r") as file:
    content = file.read();
    print(content)
    file.seek(0) 
    for line in file:
        words = line.split()
        for word in words:
            if any(char in letters for char in word):
                word_count += 1

print("Number of words containing any one of the letters ['w', 'o', 'r', 'd', 's']:", word_count)
