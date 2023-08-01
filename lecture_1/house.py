def main():
    name = input("What`s your name? ")

    match name:
        case "Harry" | "Hermione" | "Ron":
            gryffindor()
        case "Draco":
            slytherin()
        case _:
            print("Who?")

def gryffindor():
    print("Gryffindor")
    
def slytherin():
    print("Slytherin")

main()