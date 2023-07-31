# Assign value from input to variable
name = input("What`s your name? ")

# Remove whitespace from start and end of str
name = name.strip()

# Capitalize first letter of each word
name = name.title()

# Concatenation
print("Hello, " + name)

# Passing variable as argument making space automatically by sep property
print("Hello,", name)

# Interpolation with f-string
print(f"Hello, {name}")

# Another way for interpolation with format function
print("Hello, {}".format(name))

"""
    Multiline comment
    Just testing how this works :)
"""