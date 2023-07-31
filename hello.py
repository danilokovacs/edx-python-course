def main():
    # Assign value from input to variable, remove whitespace from start and end of str and capitalize first letter of each word
    name = input("What`s your name? ").strip().title()

    # Concatenation
    print("Hello, " + name)

    # Passing variable as argument making space automatically by sep property
    print("Hello,", name)

    # Interpolation with f-string
    print(f"Hello, {name}")

    # Another way for interpolation with format function
    print("Hello, {}".format(name))

    helloTo()
    helloTo("Danilo Kovacs")

    """
        Multiline comment
        Just testing how this works :)
    """

def helloTo(something="world"):
    print(f"Hello, {something}!")


main()