def reverse_case(input_string):
    result = ''
    for char in input_string:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char  # For non-alphabet characters
    return result

# Input from the user
input_string = input("Enter the string: ")
print("Reversed case:", reverse_case(input_string))
