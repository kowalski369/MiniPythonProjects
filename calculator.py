# Info

a = "Simple Arthematic calculator"
mod = a.title().center(50,"~")
print(mod)



# Taking user input
 
num1 = int(input("Enter the Number: "))
operator = input("Enter the operator: ")
num2 = int(input("Enter the Number: "))

# Making the Logic using if else statements
def main():
    if operator == "+":
        print(f"The sum of {num1} and {num2} is",num1 + num2)
    elif operator == "-":
        print(f"The difference of {num1} and {num2} is",num1 - num2)
    elif operator == "-":
        print(f"The mltiplication of {num1} and {num2} is",num1 * num2)
    elif operator == "/":
        print(f"The division of {num1} divided by {num2} is",num1 / num2)
    elif operator == "//":
        print(f"The quotient of {num1} divided by {num2} is",num1 // num2)
    elif operator == "%":
        print(f"The remainder of {num1} divided by {num2} is",num1 % num2)
    elif operator == "**":
        print(f"{num1} raised to be power {num2} is",num1 ** num2)
    else :
        print("This two digit calculator only supports these operators\n+,-,/,//(Floor-division),%(Modulous),**(Square)")


main()
