# This mini project takes the string or message and converts it into unreadble format and also takes
# unreadble format texts to convert it to readble format by this it acts like a encription


# taking user input

modes = input("Want to encript or decript\nEnter option \"a\" to encript\nEnter option \"b\" : ")

# Condition for incript or decript

if modes=="a":
    promt = input("Enter the promt: ")
    
    # Making list of words from the promt
    listedPrompt = promt.split()  


    for i in listedPrompt:
        lst = i
        if len(lst)>3:

        print(lst)

