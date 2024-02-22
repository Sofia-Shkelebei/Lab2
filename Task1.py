# Problem 1: Write a program that asks the user to enter a number
number = int(input("Please enter an integer value: "))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
print("------------------------------")

# Problem 2: Write a program that calculates the grade
ExamScore = float(input("Enter the exam score: "))
if ExamScore > 100 or ExamScore < 0:
    print("Wrong exam score!")
elif ExamScore >= 90:
    print("The grade is A")
elif ExamScore >= 80:
    print("The grade is B")
elif ExamScore >= 70:
    print("The grade is C")
elif ExamScore >= 60:
    print("The grade is D")
else:
    print("The grade is F")
print("------------------------------")


# Problem 3: Write a program that computes and outputs the nth Fibonacci number
def fibonacci(n):
    if n < 0:
        return "Invalid input"
    elif n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


element = int(input("Enter the element number of Fibonacci number: "))
print("The Fibonacci number is:", fibonacci(element))
print("------------------------------")


# Problem 4: Write a program that computes and outputs the Factorial of the number
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


Number = int(input("Enter the integer number: "))
print("The factorial of the number is:", factorial(Number))
print("------------------------------")

# Problem 5: Write a program that draws the diamond shape
rows = int(input("Enter the odd number of rows: "))
if rows % 2 == 0:
    rows += 1
    print("The number of rows is even. One additional row was added.")

for i in range(0, rows//2 + 1):
    print(" " * (rows//2 - i), "*" * (1 + 2*i))
for i in range(rows//2, 0, -1):
    print(" " * (rows//2 - i + 1), "*" * (2*i - 1))

