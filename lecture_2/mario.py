def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        for _ in range(size):
            print("#", end="")
        print()

# def print_column(num):
#     for _ in range(num):
#         print("#")

# def print_row(num):
#     for _ in range(num):
#         print("#", end="")

main()