def main():
    x = int(input("What`s x? "))

    if is_even(x):
        print(f"The number {x} is even")
    else:
        print(f"The number {x} is odd")

def is_even(x):
    return x % 2 == 0

main()