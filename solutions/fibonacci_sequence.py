# a program that generates the fibonacci sequence up to a given number of numbers 

def fib(n):
    if n <= 1:
        return n 
    else: 
        return fib(n - 1) + fib(n - 2)

nterms = int(input("How many terms of the fibonacci sequence would you like to print? (Enter an integer and try to keep it below 50): "))

if nterms <= 0:
    print("Enter a positive integer.")
else:
    print("Fibonacci sequence with the amount of your given terms: ")
    for i in range(nterms):
        print(fib(i))