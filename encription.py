# This mini project takes the string or message and converts it into unreadble format and also takes
# unreadble format texts to convert it to readble format by this it acts like a encription
import random

rndstr = "asd dgg wer dsd fgd htr vxx ujt zxc iku oii yoo sdf ass bcv dog bat fat okk wet bed"
rnd = rndstr.split()
def main():
    # taking user input

    modes = input("Want to encript or decript\nEnter option \"a\" to encript\nEnter option \"b\" to decript : ")

    # Condition for incript or decript
    
    if modes=="a":
        promt = input("Enter the promt: ")

        # Making list of words from the promt
        listedPrompt = promt.split()
        text = []
        for i in listedPrompt:
            # text = []
            if len(i)>=3 :
                i = i[1:] + i[0]
                i = (rnd[random.randint(1,20)]+ i + rnd[random.randint(1,20)])
                text.append(i)
            elif len(i)<3:
                i = i[::-1]
                text.append(i)
        
        print(" ".join(text)) # join method joins the iterable obejects with given value.
    
    elif modes == "b":
        promt = input("Enter the encripted promt: ")

        # Making list of words from the promt
        listedPrompt = promt.split()
        text = []
        for i in listedPrompt:
            if len(i)-6>=3 :
                i =  i[3:-3]
                i = i[-1] + i[:]
                i = i[:-1]
                text.append(i)
            elif len(i)<3:
                i = i[::-1]
                text.append(i)
        
        print(" ".join(text)) # join method joins the iterable obejects with given value.
    

main()