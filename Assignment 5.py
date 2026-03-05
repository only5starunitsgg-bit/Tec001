import re
pattern = r'^[A-Z]{2,3}[0-9]{3}$'
def validate_course_code(course_code):
    if re.match(pattern, course_code):
        return True
    else:
        return False
course_codes = ['TEC001', 'AU006', 'MATH202']
for code in course_codes:
    if validate_course_code(code):
        print(f"{code} is a valid course code.")
    else:
        print(f"{code} is an invalid course code.")        

#EX2:
pattern = r'^#[A-F0-9]{6}$'
def validate_hex_color(color_code):
    if re.match(pattern, color_code):
        return True
    else:
        return False
hex_colors = ['#FF0000', '#00FF00', '#0000FF', '#GGGGGG']
for color in hex_colors:
    if validate_hex_color(color):
        print(f"{color} is a valid hex color code.")
    else:
        print(f"{color} is an invalid hex color code.")        

#EX3:
pattern = r'[0-9]+'
sentence = input("Enter a sentence: ")
numbers = re.findall(pattern, sentence)
print("Sum of numbers found in the sentence:", sum(float(n) for n in numbers))

#EX4:
def redact_phone_numbers(text):
    pattern = r'(\+84\d+|\d{10})'
    redacted_text = re.sub(pattern, '[REDACTED]', text)
    return redacted_text
input_text = "Contact me at +84123456789 or 0123456789."
redacted_text = redact_phone_numbers(input_text)
print("Redacted text:", redacted_text)