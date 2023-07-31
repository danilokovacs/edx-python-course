firstNumber = int(input("What`s first number? "))
secondNumber = int(input("What`s second number? "))

print(f"The result is {firstNumber + secondNumber}")

print("--------------------------------------------")
firstFloatNumber = float(input("What`s your first float number? "))
secondFloatNumber = float(input("What`s your second float number? "))

roundedResult = round(firstFloatNumber + secondFloatNumber)

print(f"The result is {roundedResult:,}")