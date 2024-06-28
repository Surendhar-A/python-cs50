# Ask user for their name
name  = input('What is your name? ').strip().title()

"""
# Remove whitespace from start and end of string
name = name.strip()

# Capitalize the first letter of the string
name = name.capitalize()

# Captialize the first letter of each word
name = name.title()

# Remove whitespace and capitalize the string
name = name.strip().title()
"""
first , last = name.split(' ')

# Say hello to user
print('Hello',name)
print('Hello '+name)
print(f'Hello {name}')
print('Hello', first)
print('Hello', last)
