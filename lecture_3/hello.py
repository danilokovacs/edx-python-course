while True:
    try:
        x = int(input("What`s x? "))
        print(f"x is {x}")
    except ValueError:
        print("Value inputed is not integer")
    else:
        break

print(f"x is {x}")