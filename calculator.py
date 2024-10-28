x = input("Please input your first number: ")
y = input("Please input your second number: ")
z = input("Please input your operation (+, -, *, /): ")


x = float(x)
y = float(y)


if z == "+":
    res = x + y
elif z == "-":
    res = x - y
elif z == "*":
    res = x * y
elif z == "/":
    if y != 0:
        res = x / y
    else:
        res = "Error: Division by zero"
else:
    res = "Invalid operation"

print("Result:", res)

#check if user wants another calculation
# break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
        else:
            print("Invalid Input")
