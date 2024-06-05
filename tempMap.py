# this program converts the temperature of all the elements in the list and the condition is that I have to use map function to do this

def main():
    prompt = input("Enter the Celsius temperature separated by spaces to get the Fahrenheit temperature of every number: ")
    # converting input str as a list
    promlist = prompt.split()

    emptylist = []

    for i in promlist:
        emptylist.append(int(i))
    
    faren = map(lambda c: c/5 * 9 +32,emptylist)
    print(list(faren))


main()