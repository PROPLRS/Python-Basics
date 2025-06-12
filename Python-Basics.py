print("Hello from Shrish!")

name = input("What is your name: ")
age = int(input("What is your age: "))
hobby = input("What is your hobby: ")

print(f"\nHello {name} !\nYou are {age} years old.\nYour hobby is {hobby} which is very interesting!")

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