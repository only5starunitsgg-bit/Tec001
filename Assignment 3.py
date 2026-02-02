#EX1
n = 3
while n <= 1000:
    print (n)
    n = n + 3
#EX2 Convert inches to centimeters
def new_func():
   while True:
    inches = float(input("Enter length in inches: "))
    if inches < 0: 
        print("end")
        break
    centimeters = inches * 2.54
    print(f"{inches} inches is equal to {centimeters} centimeters.")
new_func()
#EX3 
def new_func1():
    def ask_number():
        max_num = None
        min_num = None
        while True:
            numbers = int(input("Enter numbers: "))
            if numbers == 0:
                print("end")
                break
            if max_num is None or numbers > max_num:
                max_num = numbers
            if min_num is None or numbers < min_num:  
                min_num = numbers

        print(f"Maximum number: {max_num}")
        print(f"Minimum number: {min_num}")

    ask_number()

new_func1()
#EX4
from pydoc import text
import random
def new_func2():
    secret_number = random.randint(1, 10)
    while True:
        try:
            guess = int(input("Guess the number between 1 and 10: "))
            if guess < 1 or guess > 10:
                print("Please guess a number within the range.")
                continue
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            elif guess == secret_number:
                print("Congratulations! You've guessed the number.")
                break
        except ValueError:
            print("Please enter a valid number.")
new_func2()
#EX5
def new_func3():
   Correct_ussername = "python"
   Correct_password = "rules"
   attempts = 0
   max_attempts = 5

   while attempts < max_attempts:
       username= input("Enter username: ")
       password= input("Enter password: ")
       if username == Correct_ussername and password == Correct_password:
           print("Welcome.")
           break
       else:
           attempts += 1
           print(f"Incorrect username or password. You have {max_attempts - attempts} attempts left.")
   if attempts >= max_attempts:
       print("Too many failed attempts. Access denied.")
new_func3()
#EX6
def new_func4():
    def get_middle_character(text):
        length = len(text)
        middle = length // 2 
        if length % 2 == 0:
            return text[middle - 1: middle + 1]
        else:
            return text[middle]
    print(get_middle_character("interview"))
new_func4()
#EX7
def new_func5():
    while True:
        user_input = input("Enter a phrase: ")
        if not user_input.strip():
            print("Please enter a non-empty phrase.")
            continue
        words = user_input.split()
        return "".join(word[0].upper() for word in words)

print(new_func5())

