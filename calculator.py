history = []

print("=== Python Calculator ===")
print("Type 'q' at any time to quit.")

while True:
    print()
    print("Choose: + - * / ** %")
    op = input("Operation: ")

    if op == "q":
        break

    if op not in ["+", "-", "*", "/", "**", "%"]:
        print("That's not a valid operation. Try again.")
        continue

    a = float(input("First number: "))
    b = float(input("Second number: "))

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            print("You can't divide by zero!")
            continue
        result = a / b
    elif op == "**":
        result = a ** b
    else:
        result = a % b

    line = str(a) + " " + op + " " + str(b) + " = " + str(result)
    print(line)
    history.append(line)

print()
print("Your calculations this session:")
for item in history:
    print(item)
print("Goodbye!")