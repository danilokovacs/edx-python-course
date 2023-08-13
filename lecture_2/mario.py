def main():
    print_column(3)
    print_row(3)

def print_column(num):
    for _ in range(num):
        print("#")

def print_row(num):
    for _ in range(num):
        print("#", end="")

main()