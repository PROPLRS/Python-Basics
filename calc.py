number_one = float(input("\nType your first value: "))
number_two = float(input("Type your second value: "))
operator = input("Type your calc operator: ")

if operator == "+":
    print(f"Your result = {number_one + number_two}")
elif operator == "-":
    print(f"Your result = {number_one - number_two}")
elif operator == "/":
    print(f"Your result = {number_one / number_two}")
elif operator == "*":
    print(f"Your result = {number_one * number_two}")
else:
    print(f"Invalid Response")
