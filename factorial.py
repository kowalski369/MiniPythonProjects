def factorial(n):
    """
    Returns factorial of a given number.
    """
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
    
num = int(input("Enter the number for factorial: "))
print(f"The factorial of {num} is",factorial(num))