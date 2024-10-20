''' 1. Write a Python function that takes a list of numbers as input and returns the sum of all even numbers in
the list.'''
import math


def sum_Of_Even(*n):
    lis = [];
    for i in n:
        if(i%2==0):
            lis.append(i)
    return lis;


print(sum_Of_Even(1,2,3,4,5,7,8,9))

'''2. Create a Python function that accepts a string and returns the reverse of that string.'''
def reverse(str):
    s = ""
    for i in str:
        s=i+s
    return s
print(reverse("Hello"))

'''3. Implement a Python function that takes a list of integers and returns a new list containing the squares of
each number.'''
def square(*n):
    lis = []
    for i in n:
        lis.append(i**2)
    return lis
print(square(1,2,3))

'''4. Write a Python function that checks if a given number is prime or not from 1 to 200.'''
def prime(n):
    if(n>0 or n<=2):
        return "number is prime"
    for i in range(2,n):

        if(n%i==0):
            return "the given number is not a prime"
        elif(i>n/2):
            return "the number is prime"
print(prime(2))
'''5. Create an iterator class in Python that generates the Fibonacci sequence up to a specified number of
terms.'''
def fib(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b
iter1 = fib(5)
lis = list(iter1)
print(lis)

# 6. Write a generator function in Python that yields the powers of 2 up to a given exponent
def powers_of_2(exponent):
    for i in range(exponent + 1):  # Include the given exponent
        yield 2 ** i  # Yield 2 raised to the current exponent

# Example usage
for value in powers_of_2(5):
    print(value)

# 7. Implement a generator function that reads a file line by line and yields each line as a string.
def read_file_line_by_line(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                yield line.strip()  # Yield each line, stripping whitespace
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'example.txt'  # Replace with your file path
for line in read_file_line_by_line(file_path):
    print(line)

# 8. Use a lambda function in Python to sort a list of tuples based on the second element of each tuple.

lis = [(1,2,10,8),(4,7,9,10),(7,3,4,5)]

sort = lambda x: sorted(x,key=lambda tup:tup[1])
print(sort(lis))

# 9. Write a Python program that uses `map()` to convert a list of temperatures from Celsius to Fahrenheit
def converter(n):
    return n*9/5+32
celList = [32,45,78,15]
fahrenheit = list(map(converter,celList));
print(fahrenheit)

# 10. Create a Python program that uses `filter()` to remove all the vowels from a given string
str = "ramterigangamailihogayi"
vowels = 'aeiouAEIOU'
vowel = filter(lambda x:x not in vowels,str)
print(list(vowel))


# 11

# List of orders with [Order Number, Book Title and Author, Quantity, Price per Item]
orders = [
    [34587, "Learning Python, Mark Lutz", 4, 40.95],
    [98762, "Programming Python, Mark Lutz", 5, 56.80],
    [77226, "Head First Python, Paul Barry", 3, 32.95],
    [88112, "Einführung in Python3, Bernd Klein", 3, 24.99]
]

# Lambda function to calculate order total and apply the 10€ increase if total is less than 100
calculate_total = lambda order: (order[0], order[2] * order[3] + (10 if order[2] * order[3] < 100 else 0))

# Use map() to apply the lambda function to each order
final_totals = list(map(calculate_total, orders))

# Print the final list of (Order Number, Total Price)
print(final_totals)
