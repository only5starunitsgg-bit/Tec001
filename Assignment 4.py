#EX1
empty_list = []
while True:
    numbers = input("Enter a series of numbers: ")
    if numbers == "":
        break
    empty_list.append(float(numbers))
    empty_list.sort(reverse=True)
print("Five greatest numbers:", empty_list[:5])
#EX2
import math

while True:
  try:
    user_number = input("Enter an integer: ")
    is_prime = True
    if user_number == "quit":
       print("Exiting the program.")
       break
    user_number = int(user_number)
    if user_number < 0:
        is_prime = False
    else:
        for i in range(2, math.isqrt(user_number) +1):
            if user_number % i == 0:
                is_prime = False
    if is_prime:
        print(f"{user_number} is a prime number.")
    else:
        print(f"{user_number} is not a prime number.")
  except ValueError:
        print("That's not an integer. Please try again.")
#EX3
def ex_cities():
     cities = []
     for i in range(5):
         name= input("Enter a city name: ")
         cities.append(name)
     for city in cities:
        print(city)
ex_cities()
#EX4
def caculate_sum(number_list):
    return sum(number_list)
def main():
    intergers = []
    while True:
        user_input = input("Enter an integer (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            number = int(user_input)
            intergers.append(number)
        except ValueError:
            print("Invalid input. Please enter an integer.")
    if intergers:
        total = caculate_sum(intergers)
        print(f"Sum of integers: {total}")
    else:
        print("No integers were entered.")
main()
caculate_sum()

#EX5
def remove_uneven_numbers(num_list):
    even_numbers = []
    for num in num_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
def main():
    numbers = []
    while True:
        user_input = input("Enter an integer (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter an integer.")
    even_numbers_list = remove_uneven_numbers(numbers)
    print(f"Even numbers: {even_numbers_list}")
main()
remove_uneven_numbers()
