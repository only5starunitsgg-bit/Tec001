#EX1:
import numbers


def main():
    numbers = []

    while True:
        user_input = input("Enter a number (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a number or 'done' to finish.")

numbers.sort(reverse=True)
top_five = numbers[:5]
print("The five largest numbers are:")
for num in top_five:
    print(num)
if __name__ == "__main__":    main()
#EX2:
def main():
    seasons = ["Spring", "Summer", "Autumn", "Winter"]
    months = int(input("Enter the months (1-12): "))
    if months in [3, 4, 5]:
       print("The season is Spring.")
    elif months in [6, 7, 8]:
        print("The season is Summer.")
    elif months in [9, 10, 11]:
        print("The season is Autumn.")
    elif months in [12, 1, 2]:
        print("The season is Winter.")
    else:
        print("Invalid month. Please enter a number between 1 and 12.")
    print("The seasons is:", seasons)
if __name__ == "__main__":    main()
#EX3:
def main():
    names = set()
    while True:
        user_input = input("Enter a name (or press Enter to quit): ")
        if user_input == "":
            break
        if user_input in names:
            print("Existing name")
        else:
            print("New name")
            names.add(user_input)

    print("\nList of names entered:")
    for name in names:
        print(name)
if __name__ == "__main__":
    main()
#EX4:
from collections import Counter

def word_frequency_analysis(text):

    words = text.lower().split()

    freq = Counter(words)

    top_five = freq.most_common(5)
 
    total_words = len(words)

    top_five_total = sum(count for _, count in top_five)

    proportion = (top_five_total / total_words) * 100 if total_words > 0 else 0

    print("Top 5:", dict(top_five))
    print("Total number of words:", total_words)
    print(f"Proportion of 5 most common words: {top_five_total} / {total_words} = {proportion:.2f}%")

sample_text = "the world is mine the world is out the world is the mine out out"
word_frequency_analysis(sample_text)
#EX5:
def remove_odds(numbers):
    """Return a new list with all odd numbers removed."""
    return [num for num in numbers if num % 2 == 0]

def main():
    # Example list for testing
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Call the function
    even_list = remove_odds(original_list)

    # Print both lists
    print("Original list:", original_list)
    print("List without odd numbers:", even_list)
if __name__ == "__main__":
    main()
