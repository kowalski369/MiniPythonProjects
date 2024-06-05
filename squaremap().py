# this program takes the numbers as inut and squares all the number the condition is that I have to make this program using map() function and lambda function.

def main():
    # taking user input as string and converting it to list
    prompt = input("Enter the numbers separated by spaces to get the square of every number: ")
    # converting input str as a list
    promlist = prompt.split()

    emptylist = []

    for i in promlist:
        emptylist.append(int(i))



    square = map(lambda x: x**2,emptylist)
    print(list(square))


main()