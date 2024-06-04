# The program takes the user input and returns the reverse value of it.

def reverseInput():
    prompt = input("Enter the prompt: ")
    return prompt[::-1]


print(reverseInput())
