while True:
    try:
        x = int(input("What`s x? "))
        break
    except ValueError:
        # we can use the work "pass" to just pass and not throw any exception
        print("Value inputed is not integer")
    # else:
    #     break

print(f"x is {x}")