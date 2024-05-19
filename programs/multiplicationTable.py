# Multiplication table:
import introJitendra
introJitendra.printIntro("Multiplication table:")
def multiplication_table(n):
    for i in range(1, 11):
        print(n, 'x', i, '=', n*i)

n = int(input('enter number : '))
multiplication_table(n)