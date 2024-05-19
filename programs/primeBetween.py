#  Python function print all prime numbers between two distinct number.
import introJitendra
introJitendra.printIntro("Python function print all prime numbers between two distinct number.")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_between(start, end):
    print(f"prime between {start} and {end} are : ")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

start_num = int(input("enter from number : "))
end_num = int(input("enter end number : "))
print_primes_between(start_num, end_num)
